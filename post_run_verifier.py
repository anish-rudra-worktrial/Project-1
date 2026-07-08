#!/usr/bin/env python3
"""Post-run verification triage for Fleet Project One.

This script turns completed-run evidence into an actionable review queue. It is
intentionally transparent: the model/session has already run, and this layer
parses trace notes or downloaded transcripts, then classifies the observed
outcome with auditable rules.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any


BUCKET_HEADINGS = {
    "A: Likely Good Spot Check": "A_likely_good_spot_check",
    "B: Close / Verify Derivability": "B_close_verify_derivability",
    "C: Repair Candidate": "C_repair_candidate",
    "D: High-Risk Manual Review": "D_high_risk_manual_review",
}

POST_RUN_ACTIONS = {
    "PASS_CLEAN": "Promote or keep in the near-promote queue after normal spot-check.",
    "PASS_BUT_STATIC_RISK": "Promote only after one extra human spot-check because static risk was high.",
    "NARROW_VERIFIER_FAILURE": "Repair the specific verifier/state mismatch, then rerun.",
    "PARTIAL_COMPLETION": "Repair missing final side effects or rerun with focused review.",
    "ENVIRONMENT_OR_NAVIGATION_FAILURE": "Separate environment/tooling issue from task quality before rejecting.",
    "TASK_OR_SEED_AMBIGUITY": "Manual prompt/seed review first; clarify the intended unique answer.",
    "BROAD_SIDE_EFFECT_FAILURE": "Keep in manual review or major repair; too many durable effects failed.",
    "UNSCORED_OR_TRACE_UNAVAILABLE": "Inspect the trace manually before making a delivery decision.",
}

POST_RUN_ORDER = {
    "PASS_CLEAN": 0,
    "PASS_BUT_STATIC_RISK": 1,
    "NARROW_VERIFIER_FAILURE": 2,
    "PARTIAL_COMPLETION": 3,
    "ENVIRONMENT_OR_NAVIGATION_FAILURE": 4,
    "TASK_OR_SEED_AMBIGUITY": 5,
    "BROAD_SIDE_EFFECT_FAILURE": 6,
    "UNSCORED_OR_TRACE_UNAVAILABLE": 7,
}

TASK_RE = re.compile(r"\btask_[A-Za-z0-9_]+")
UUID_RE = re.compile(
    r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b",
    re.IGNORECASE,
)
SCORE_RE = re.compile(r"\bscore\b[^0-9]{0,40}([01](?:\.\d+)?)", re.IGNORECASE)
MODEL_RE = re.compile(
    r"\b(?:gpt-[A-Za-z0-9_.-]+|claude-[A-Za-z0-9_.-]+|gemini-[A-Za-z0-9_.-]+|"
    r"o[0-9][A-Za-z0-9_.-]*)\b",
    re.IGNORECASE,
)

AMBIGUITY_TERMS = [
    "ambiguity",
    "ambiguous",
    "no single",
    "unresolved conflict",
    "could not determine",
    "inconsistent",
    "constraints",
    "seed inconsistency",
]
ENVIRONMENT_TERMS = [
    "navigation",
    "tool failure",
    "tool failures",
    "blocked",
    "could not complete",
    "inaccessible",
    "did not register",
    "environment",
    "ui failure",
    "flow blockage",
]
BROAD_TERMS = [
    "broad",
    "multi-system",
    "too many side effects",
    "no expected transfer",
    "no transfer",
    "no transaction records",
    "wrong account balances",
    "unchanged balances",
    "missing zelle transaction",
    "missing savings transfer",
    "missing credit-card payment",
]
NARROW_TERMS = [
    "failed narrowly",
    "concrete state mismatch",
    "diff failure",
    "unexpected extra",
    "expected exactly",
    "final failure was specific",
    "transfer mismatch",
    "draft instead of sent",
    "send-state issue",
]
PARTIAL_TERMS = [
    "partial success",
    "partial completion",
    "mixed result",
    "mostly correct",
    "confirmed",
    "but",
    "missing final",
]


def normalize_space(value: str) -> str:
    return " ".join(value.strip().split())


def clean_markdown_cell(value: str) -> str:
    cleaned = re.sub(r"`([^`]*)`", r"\1", value.strip())
    return normalize_space(cleaned)


def task_prefix(value: str) -> str:
    cleaned = clean_markdown_cell(value).replace("...", "")
    match = TASK_RE.search(cleaned)
    return match.group(0) if match else cleaned


def parse_score_model(value: str) -> tuple[float | None, str]:
    tokens = re.findall(r"`([^`]+)`", value)
    score: float | None = None
    model = ""
    for token in tokens:
        stripped = token.strip()
        if re.fullmatch(r"[01](?:\.\d+)?", stripped):
            score = float(stripped)
        elif MODEL_RE.search(stripped):
            model = MODEL_RE.search(stripped).group(0)
    if score is None:
        match = re.search(r"\b([01](?:\.\d+)?)\b", value)
        if match:
            score = float(match.group(1))
    if not model:
        match = MODEL_RE.search(value)
        if match:
            model = match.group(0)
    return score, model


def load_triage(path: Path | None) -> tuple[dict[str, dict[str, str]], list[dict[str, str]]]:
    if not path:
        return {}, []
    with path.open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    return {row["key"]: row for row in rows}, rows


def find_triage_row(
    task_ref: str,
    triage_by_key: dict[str, dict[str, str]],
    triage_rows: list[dict[str, str]],
) -> tuple[dict[str, str] | None, str]:
    prefix = task_prefix(task_ref)
    if prefix in triage_by_key:
        return triage_by_key[prefix], "exact"
    matches = [row for row in triage_rows if row.get("key", "").startswith(prefix)]
    if len(matches) == 1:
        return matches[0], "prefix"
    if len(matches) > 1:
        return matches[0], f"ambiguous_prefix_{len(matches)}"
    return None, "not_found"


def term_count(text: str, terms: list[str]) -> int:
    lowered = text.lower()
    return sum(1 for term in terms if term in lowered)


def classify_outcome(
    score: float | None,
    evidence: str,
    handoff_call: str,
    static_bucket: str,
    static_risk_score: str,
) -> tuple[str, str]:
    text = f"{evidence} {handoff_call}".lower()

    high_static_risk = static_bucket.startswith("D_")
    try:
        high_static_risk = high_static_risk or float(static_risk_score) >= 8.0
    except (TypeError, ValueError):
        pass

    if score is not None and score >= 0.999:
        if high_static_risk:
            return "PASS_BUT_STATIC_RISK", "high"
        return "PASS_CLEAN", "high"

    if not text.strip() and score is None:
        return "UNSCORED_OR_TRACE_UNAVAILABLE", "low"

    if term_count(text, AMBIGUITY_TERMS):
        return "TASK_OR_SEED_AMBIGUITY", "high"
    if term_count(text, ENVIRONMENT_TERMS):
        return "ENVIRONMENT_OR_NAVIGATION_FAILURE", "high"
    explicit_partial = "partial success" in text or "mixed result" in text
    explicit_broad = "broad" in text or "multi-system" in text or "too many side effects" in text

    if explicit_partial:
        return "PARTIAL_COMPLETION", "high"
    if explicit_broad:
        return "BROAD_SIDE_EFFECT_FAILURE", "high"
    if term_count(text, NARROW_TERMS):
        return "NARROW_VERIFIER_FAILURE", "high"
    if "mostly correct" in text or ("confirmed" in text and "but" in text):
        return "PARTIAL_COMPLETION", "medium"
    if term_count(text, BROAD_TERMS) >= 2 or text.count("missing ") >= 4:
        return "BROAD_SIDE_EFFECT_FAILURE", "high"
    if score is None:
        return "UNSCORED_OR_TRACE_UNAVAILABLE", "low"
    return "NARROW_VERIFIER_FAILURE", "medium"


def parse_trace_evidence(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    current_bucket = ""
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line.startswith("## "):
            heading = line.removeprefix("## ").strip()
            current_bucket = BUCKET_HEADINGS.get(heading, current_bucket)
            continue
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) < 6 or not cells[0].strip().isdigit():
            continue
        score, model = parse_score_model(cells[3])
        rows.append(
            {
                "source": str(path),
                "source_type": "trace_evidence_markdown",
                "rank": int(cells[0]),
                "static_bucket": current_bucket,
                "task_ref": clean_markdown_cell(cells[1]),
                "session_id": clean_markdown_cell(cells[2]),
                "score": score,
                "model": model,
                "evidence_summary": clean_markdown_cell(cells[4]),
                "handoff_call": clean_markdown_cell(cells[5]),
            }
        )
    return rows


def stringify_json(value: Any) -> str:
    if isinstance(value, dict):
        preferred_keys = [
            "task",
            "task_key",
            "session",
            "session_id",
            "score",
            "model",
            "verifier_output",
            "final_answer",
            "transcript",
            "messages",
            "events",
        ]
        parts = []
        for key in preferred_keys:
            if key in value:
                parts.append(f"{key}: {stringify_json(value[key])}")
        if parts:
            return "\n".join(parts)
    return json.dumps(value, ensure_ascii=True, indent=2)


def transcript_summary(text: str, limit: int = 900) -> str:
    signal_re = re.compile(
        r"\b(score|verifier|failed|failure|passed|success|missing|unexpected|wrong|"
        r"draft|sent|ambigu|navigation|blocked|tool failure|could not|no expected|"
        r"no new|unchanged|did not register)\b",
        re.IGNORECASE,
    )
    signal_lines = [
        normalize_space(line)
        for line in text.splitlines()
        if signal_re.search(line) and normalize_space(line)
    ]
    summary = " ".join(signal_lines[:8])
    if not summary:
        summary = normalize_space(text[-limit:])
    return summary[:limit]


def parse_transcript_file(path: Path) -> dict[str, Any]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    text = raw
    if path.suffix.lower() == ".json":
        try:
            text = stringify_json(json.loads(raw))
        except json.JSONDecodeError:
            pass

    task_match = TASK_RE.search(text) or TASK_RE.search(path.stem)
    session_match = UUID_RE.search(text) or UUID_RE.search(path.stem)
    score_match = SCORE_RE.search(text)
    model_match = MODEL_RE.search(text)

    return {
        "source": str(path),
        "source_type": "downloaded_transcript",
        "rank": "",
        "static_bucket": "",
        "task_ref": task_match.group(0) if task_match else "",
        "session_id": session_match.group(0) if session_match else path.stem,
        "score": float(score_match.group(1)) if score_match else None,
        "model": model_match.group(0) if model_match else "",
        "evidence_summary": transcript_summary(text),
        "handoff_call": "",
    }


def parse_transcript_dir(path: Path) -> list[dict[str, Any]]:
    allowed_suffixes = {".txt", ".md", ".json"}
    rows = []
    for child in sorted(path.rglob("*")):
        if child.is_file() and child.suffix.lower() in allowed_suffixes:
            rows.append(parse_transcript_file(child))
    return rows


def enrich_rows(
    rows: list[dict[str, Any]],
    triage_by_key: dict[str, dict[str, str]],
    triage_rows: list[dict[str, str]],
) -> list[dict[str, Any]]:
    enriched = []
    for row in rows:
        triage_row, match_status = find_triage_row(row.get("task_ref", ""), triage_by_key, triage_rows)
        if triage_row:
            static_bucket = row.get("static_bucket") or triage_row.get("bucket", "")
            task_key = triage_row.get("key", "")
            risk_score = triage_row.get("risk_score", "")
            completed_sessions = triage_row.get("completed_sessions", "")
            env_id = triage_row.get("env_id", "")
            findings = triage_row.get("findings", "")
        else:
            static_bucket = row.get("static_bucket", "")
            task_key = ""
            risk_score = ""
            completed_sessions = ""
            env_id = ""
            findings = ""

        category, confidence = classify_outcome(
            row.get("score"),
            str(row.get("evidence_summary", "")),
            str(row.get("handoff_call", "")),
            static_bucket,
            risk_score,
        )

        score = row.get("score")
        enriched.append(
            {
                "post_run_priority": "",
                "post_run_category": category,
                "recommended_action": POST_RUN_ACTIONS[category],
                "confidence": confidence,
                "score": "" if score is None else f"{score:.2f}",
                "model": row.get("model", ""),
                "rank": row.get("rank", ""),
                "static_bucket": static_bucket,
                "static_risk_score": risk_score,
                "env_id": env_id,
                "completed_sessions": completed_sessions,
                "task_ref": row.get("task_ref", ""),
                "task_key": task_key,
                "task_match_status": match_status,
                "session_id": row.get("session_id", ""),
                "evidence_summary": row.get("evidence_summary", ""),
                "handoff_call": row.get("handoff_call", ""),
                "static_findings": findings,
                "source_type": row.get("source_type", ""),
                "source": row.get("source", ""),
            }
        )

    enriched.sort(
        key=lambda item: (
            POST_RUN_ORDER.get(str(item["post_run_category"]), 99),
            int(item["rank"]) if str(item["rank"]).isdigit() else 999999,
            str(item["task_ref"]),
        )
    )
    for index, row in enumerate(enriched, start=1):
        row["post_run_priority"] = index
    return enriched


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        return
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, rows: list[dict[str, Any]]) -> None:
    path.write_text(json.dumps(rows, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def write_summary(path: Path, rows: list[dict[str, Any]], trace_sources: list[str]) -> None:
    category_counts = Counter(row["post_run_category"] for row in rows)
    bucket_counts = Counter(row["static_bucket"] or "unknown" for row in rows)
    pass_count = sum(1 for row in rows if row["score"] and float(row["score"]) >= 1.0)
    fail_count = sum(1 for row in rows if row["score"] and float(row["score"]) < 1.0)
    unscored_count = sum(1 for row in rows if not row["score"])

    lines = [
        "# Post-Run Verification Summary",
        "",
        "This report classifies completed model-run evidence after the task has already been executed. It is a post-run QA layer, not a model runner and not an LLM judge.",
        "",
        "## Inputs",
        "",
    ]
    if trace_sources:
        for source in trace_sources:
            lines.append(f"- `{source}`")
    else:
        lines.append("- No input rows parsed.")

    lines.extend(
        [
            "",
            "## Coverage",
            "",
            f"- Parsed rows: {len(rows)}",
            f"- Passing scored rows: {pass_count}",
            f"- Failing scored rows: {fail_count}",
            f"- Unscored or missing-score rows: {unscored_count}",
            "",
            "## Post-Run Categories",
            "",
            "| Category | Count | Action |",
            "| --- | ---: | --- |",
        ]
    )
    for category in sorted(POST_RUN_ACTIONS, key=lambda key: POST_RUN_ORDER[key]):
        lines.append(f"| `{category}` | {category_counts.get(category, 0)} | {POST_RUN_ACTIONS[category]} |")

    lines.extend(["", "## Static Bucket Coverage", "", "| Static bucket | Parsed rows |", "| --- | ---: |"])
    for bucket, count in sorted(bucket_counts.items()):
        lines.append(f"| `{bucket}` | {count} |")

    lines.extend(
        [
            "",
            "## Highest-Signal Rows",
            "",
            "| Priority | Category | Task | Session | Score | Evidence |",
            "| ---: | --- | --- | --- | ---: | --- |",
        ]
    )
    for row in rows[:12]:
        evidence = str(row["evidence_summary"]).replace("|", "/")
        if len(evidence) > 170:
            evidence = evidence[:167] + "..."
        lines.append(
            f"| {row['post_run_priority']} | `{row['post_run_category']}` | "
            f"`{row['task_ref']}` | `{row['session_id']}` | {row['score'] or 'n/a'} | {evidence} |"
        )

    lines.extend(
        [
            "",
            "## How To Use This",
            "",
            "1. Start with `PASS_CLEAN` and `PASS_BUT_STATIC_RISK` rows for promotion candidates.",
            "2. Route `NARROW_VERIFIER_FAILURE` rows to targeted verifier or final-state repair.",
            "3. Treat `PARTIAL_COMPLETION` rows as close runs that need missing side effects repaired or rerun.",
            "4. Separate `ENVIRONMENT_OR_NAVIGATION_FAILURE` from true task-quality failures before rejecting.",
            "5. Keep `TASK_OR_SEED_AMBIGUITY` and `BROAD_SIDE_EFFECT_FAILURE` in manual review.",
            "",
            "## Limits",
            "",
            "- Markdown trace rows are manually curated evidence; downloaded transcripts provide broader scale.",
            "- The classifier is rule-based and intentionally explainable, so edge cases should be reviewed by a human.",
            "- If a task key is shortened in the evidence file, the triage join uses best-effort prefix matching.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Classify completed-run traces into post-run QA categories."
    )
    parser.add_argument(
        "--trace-evidence",
        type=Path,
        help="Markdown trace evidence file, such as trace_evidence.md.",
    )
    parser.add_argument(
        "--transcript-dir",
        type=Path,
        help="Directory of downloaded completed-session transcripts (.txt, .md, .json).",
    )
    parser.add_argument(
        "--triage-csv",
        type=Path,
        help="Optional reports/task_triage.csv for static bucket/risk joins.",
    )
    parser.add_argument("--out-dir", type=Path, default=Path("reports"))
    return parser


def main() -> None:
    parser = build_arg_parser()
    args = parser.parse_args()

    if not args.trace_evidence and not args.transcript_dir:
        parser.error("Provide --trace-evidence, --transcript-dir, or both.")

    rows: list[dict[str, Any]] = []
    sources: list[str] = []
    if args.trace_evidence:
        rows.extend(parse_trace_evidence(args.trace_evidence))
        sources.append(str(args.trace_evidence))
    if args.transcript_dir:
        rows.extend(parse_transcript_dir(args.transcript_dir))
        sources.append(str(args.transcript_dir))

    triage_by_key, triage_rows = load_triage(args.triage_csv)
    enriched = enrich_rows(rows, triage_by_key, triage_rows)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    write_csv(args.out_dir / "post_run_verification.csv", enriched)
    write_json(args.out_dir / "post_run_verification.json", enriched)
    write_summary(args.out_dir / "post_run_verification_summary.md", enriched, sources)

    print(f"Parsed {len(enriched)} completed-run evidence rows.")
    print(f"Wrote {args.out_dir / 'post_run_verification.csv'}")
    print(f"Wrote {args.out_dir / 'post_run_verification.json'}")
    print(f"Wrote {args.out_dir / 'post_run_verification_summary.md'}")


if __name__ == "__main__":
    main()
