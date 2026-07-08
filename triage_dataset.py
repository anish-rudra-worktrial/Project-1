#!/usr/bin/env python3
"""Static QA triage for Fleet Project One task datasets.

The script intentionally produces leads for human review. It does not decide
whether a task is deliverable by itself; it makes the repetitive first pass
consistent and auditable.
"""

from __future__ import annotations

import argparse
import ast
import csv
import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean, median
from typing import Any


APP_PATTERNS = {
    "harbor": [
        r"\bHarbor\b",
        r"\bBank of Harbor\b",
        r"\bEveryday Checking\b",
        r"\bEmergency Savings\b",
        r"\bZelle\b",
    ],
    "meridian": [
        r"\bMeridian\b",
        r"\bGold Card\b",
        r"\bRewards Card\b",
        r"\bPay Over Time\b",
        r"\bAutopay\b",
        r"\bAutoPay\b",
    ],
    "quickbooks": [
        r"\bLedger\b",
        r"\bQuickBooks\b",
        r"\binvoice\b",
        r"\bbill\b",
        r"\bvendor\b",
        r"\bcontractor\b",
    ],
    "outlook": [
        r"\bOutlook\b",
        r"\bemail\b",
        r"\binbox\b",
        r"\breply\b",
        r"\bforward\b",
        r"\bsender\b",
        r"\bsubject\b",
    ],
    "fakelook": [
        r"\bLatch\b",
        r"\bcalendar\b",
        r"\bTo Do\b",
        r"\btask list\b",
        r"\bmessage through Latch\b",
    ],
    "medora": [
        r"\bMedora\b",
        r"\bdoctor\b",
        r"\bappointment\b",
        r"\bprovider\b",
        r"\bvideo visit\b",
        r"\bvisit\b",
    ],
    "lifeline": [
        r"\bLifeline\b",
        r"\bprescription\b",
        r"\bmedication\b",
        r"\binsurance\b",
        r"\bPCP\b",
        r"\bhealth record\b",
    ],
}


APP_FAMILIES = {
    "fakelook": "communications",
    "outlook": "communications",
    "quickbooks": "ledger",
    "harbor": "harbor",
    "meridian": "meridian",
    "medora": "medora",
    "lifeline": "lifeline",
}


DEPENDENCY_PATTERNS = {
    "email_source": [
        r"\bemail\b",
        r"\binbox\b",
        r"\bflagged\b",
        r"\bsender\b",
        r"\bsubject\b",
        r"\breply\b",
        r"\bforward\b",
    ],
    "calendar_source": [
        r"\bcalendar\b",
        r"\bevent\b",
        r"\breminder\b",
        r"\bappointment\b",
        r"\bschedule\b",
    ],
    "bank_transactions": [
        r"\btransaction\b",
        r"\bstatement\b",
        r"\bchecking\b",
        r"\bsavings\b",
        r"\btransfer\b",
        r"\bbalance\b",
    ],
    "credit_card": [
        r"\bcredit card\b",
        r"\bMeridian\b",
        r"\bcard\b",
        r"\brewards points\b",
        r"\bAutoPay\b",
        r"\bPay Over Time\b",
    ],
    "invoice_bill": [
        r"\binvoice\b",
        r"\bbill\b",
        r"\bvendor\b",
        r"\bLedger\b",
        r"\bQuickBooks\b",
    ],
    "provider_search": [
        r"\bdoctor\b",
        r"\bspecialist\b",
        r"\bprovider\b",
        r"\baccepting new patients\b",
        r"\bin-network\b",
        r"\bsponsored\b",
    ],
    "medical_record": [
        r"\bLifeline\b",
        r"\bmedication\b",
        r"\bprescription\b",
        r"\binsurance\b",
        r"\bpatient\b",
        r"\bhealth questionnaire\b",
    ],
    "personal_profile": [
        r"\bprofile\b",
        r"\baddress\b",
        r"\bphone\b",
        r"\bemail on file\b",
        r"\bsalary\b",
        r"\bincome\b",
    ],
    "math_or_aggregation": [
        r"\btotal\b",
        r"\bsum\b",
        r"\baverage\b",
        r"\brounded\b",
        r"\bnearest\b",
        r"\bpercent\b",
        r"\b%\b",
        r"\bhighest\b",
        r"\bmost frequently\b",
    ],
    "conditional_branch": [
        r"\bif\b",
        r"\bunless\b",
        r"\botherwise\b",
        r"\bonly if\b",
    ],
}


RELATIVE_DATE_PATTERN = re.compile(
    r"\b(today|yesterday|tomorrow|next week|last week|this week|this month|"
    r"current date|a few days ago|next month|last month|day after)\b",
    re.IGNORECASE,
)
CONDITIONAL_PATTERN = re.compile(r"\b(if|unless|otherwise|only if)\b", re.IGNORECASE)
LOOKUP_PATTERN = re.compile(
    r"\b(find|locate|look for|review|search|filter|identify|extract|check|"
    r"determine|calculate|compare|pull)\b",
    re.IGNORECASE,
)
MONEY_PATTERN = re.compile(r"\$\s?\d[\d,]*(?:\.\d{1,2})?")
PHONE_PATTERN = re.compile(r"\b(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]\d{3}[-.\s]\d{4}\b")
EMAIL_PATTERN = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)
ABS_DATE_PATTERN = re.compile(
    r"\b(?:\d{1,2}/\d{1,2}(?:/\d{2,4})?|\d{4}-\d{2}-\d{2}|"
    r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*\.?\s+\d{1,2})\b",
    re.IGNORECASE,
)


NOISE_LITERAL_PARTS = {
    "ERROR_ACCUMULATOR",
    "SUCCESS_ACCUMULATOR",
    "created_at",
    "updated_at",
    "sqlite_sequence",
    "current",
    "seed",
    "expected",
    "actual",
    "database",
    "Verified",
    "Unexpected",
    "TASK_FAILED_SCORE",
    "TASK_SUCCESSFUL_SCORE",
}


NOISE_LITERAL_PATTERNS = [
    re.compile(pattern, re.IGNORECASE)
    for pattern in [
        r"\bgot\b",
        r"\bexpected\b",
        r"\bactual\b",
        r"\bverify\b",
        r"\bvalidate\b",
        r"\bverified\b",
        r"\bcombined\b",
        r"\breturning\b",
        r"\berror\b",
        r"\bguard",
        r"\bscore\b",
        r"\brow\b",
        r"\bcount\b",
        r"\bfound\b",
        r"\bshould\b",
        r"\bdatabase\b",
        r"\bapp\s+\w+",
        r"<<<|>>>",
        r"\{|\}|\[C\]|\[X\]",
        r"^['\",;:.()\-\s]+",
        r"['\",;:()\-]\s*$",
    ]
]


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def count_patterns(text: str, patterns: list[str]) -> int:
    return sum(1 for pattern in patterns if re.search(pattern, text, re.IGNORECASE))


def matched_keys(text: str, pattern_map: dict[str, list[str]]) -> list[str]:
    return sorted(
        key for key, patterns in pattern_map.items() if count_patterns(text, patterns) > 0
    )


def extract_verifier_apps(verifier: str) -> list[str]:
    apps = set(re.findall(r"""env\.app\(["']([^"']+)["']\)""", verifier))
    return sorted(apps)


def normalize_amount(amount: str) -> str:
    return amount.replace("$", "").replace(",", "").replace(" ", "")


def amount_literals_from_verifier(verifier: str) -> set[str]:
    # Keep only money-looking two-decimal literals to avoid swamping the signal
    # with ids, dates, row counts, and score constants.
    found = set()
    for raw in re.findall(r"(?<![\w.])\d{1,6}\.\d{1,2}(?![\w.])", verifier):
        try:
            value = float(raw)
        except ValueError:
            continue
        if 5.0 <= value <= 250000:
            found.add(f"{value:.2f}".rstrip("0").rstrip("."))
    return found


def string_literals_from_verifier(verifier: str) -> list[str]:
    try:
        tree = ast.parse(verifier)
    except SyntaxError:
        return []

    literals: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            value = " ".join(node.value.strip().split())
            if not value or len(value) < 6:
                continue
            if any(part in value for part in NOISE_LITERAL_PARTS):
                continue
            if re.fullmatch(r"[a-z_]+", value):
                continue
            if value.count("_") >= 2:
                continue
            literals.add(value)
    return sorted(literals)


def natural_verifier_literals_not_in_prompt(prompt: str, verifier: str) -> list[str]:
    normalized_prompt = prompt.lower()
    candidates = []
    for literal in string_literals_from_verifier(verifier):
        lower = literal.lower()
        if lower in normalized_prompt:
            continue
        if literal.startswith("[") or literal.startswith(">>>"):
            continue
        if any(pattern.search(literal) for pattern in NOISE_LITERAL_PATTERNS):
            continue
        # Prefer things that look like user-visible values over implementation
        # strings: names, messages, emails, phones, addresses, or multi-word labels.
        title_words = re.findall(r"\b[A-Z][a-z]+(?:'[a-z]+)?\b", literal)
        looks_user_visible = (
            EMAIL_PATTERN.search(literal)
            or PHONE_PATTERN.search(literal)
            or ABS_DATE_PATTERN.search(literal)
            or len(title_words) >= 2
        )
        if not looks_user_visible:
            continue
        if len(literal) > 120:
            literal = literal[:117] + "..."
        candidates.append(literal)
    return candidates[:12]


def canonical_app_families(apps: list[str]) -> list[str]:
    return sorted({APP_FAMILIES.get(app, app) for app in apps})


def prompt_summary(prompt: str, limit: int = 220) -> str:
    squashed = " ".join(prompt.split())
    return squashed if len(squashed) <= limit else squashed[: limit - 3] + "..."


def score_task(
    row: dict[str, Any], session_stats: dict[str, dict[str, Any]] | None = None
) -> dict[str, Any]:
    prompt = row.get("prompt") or ""
    verifier = row.get("verifier_func") or ""
    env_vars = row.get("env_variables") or {}
    metadata = row.get("metadata") or {}
    sessions = (session_stats or {}).get(row.get("key"), {})

    prompt_apps = matched_keys(prompt, APP_PATTERNS)
    verifier_apps = extract_verifier_apps(verifier)
    prompt_app_families = canonical_app_families(prompt_apps)
    verifier_app_families = canonical_app_families(verifier_apps)
    dependencies = matched_keys(prompt, DEPENDENCY_PATTERNS)

    relative_dates = RELATIVE_DATE_PATTERN.findall(prompt)
    absolute_dates = ABS_DATE_PATTERN.findall(prompt)
    conditionals = CONDITIONAL_PATTERN.findall(prompt)
    lookups = LOOKUP_PATTERN.findall(prompt)
    prompt_amounts = {normalize_amount(x) for x in MONEY_PATTERN.findall(prompt)}
    verifier_amounts = amount_literals_from_verifier(verifier)
    verifier_only_amounts = sorted(verifier_amounts - prompt_amounts)[:12]
    verifier_only_literals = natural_verifier_literals_not_in_prompt(prompt, verifier)

    missing_prompt_apps = sorted(set(prompt_app_families) - set(verifier_app_families))
    verifier_extra_apps = sorted(set(verifier_apps) - set(prompt_apps))
    # These are commonly no-change guard verifiers. They still matter, but the
    # absence of a prompt mention is less suspicious.
    extra_no_change_guard_apps = [
        app for app in verifier_extra_apps if app in {"fakelook", "outlook", "harbor", "meridian"}
    ]

    findings: list[str] = []
    if relative_dates:
        findings.append("RELATIVE_DATE_ANCHORS")
    if len(dependencies) >= 5:
        findings.append("MANY_CROSS_SYSTEM_DEPENDENCIES")
    if len(conditionals) >= 3:
        findings.append("HIGH_BRANCHING")
    if len(lookups) >= 5:
        findings.append("MANY_LOOKUPS")
    if missing_prompt_apps:
        findings.append("PROMPT_APP_NOT_VERIFIED")
    if len(verifier_only_amounts) >= 2:
        findings.append("VERIFIER_ONLY_AMOUNTS")
    if len(verifier_only_literals) >= 4:
        findings.append("VERIFIER_ONLY_USER_VALUES")
    if len(prompt) > 2600:
        findings.append("LONG_PROMPT")
    if any(dep in dependencies for dep in ["medical_record", "provider_search"]):
        findings.append("HEALTH_PRIVACY_REVIEW")
    if any(dep in dependencies for dep in ["bank_transactions", "credit_card", "invoice_bill"]):
        findings.append("FINANCE_SIDE_EFFECT_REVIEW")

    risk_score = 0.0
    risk_score += min(len(dependencies), 8) * 0.55
    risk_score += min(len(conditionals), 6) * 0.65
    risk_score += min(len(lookups), 8) * 0.35
    risk_score += 1.0 if relative_dates else 0.0
    risk_score += min(len(missing_prompt_apps), 4) * 1.25
    risk_score += min(len(verifier_only_amounts), 5) * 0.45
    risk_score += min(len(verifier_only_literals), 8) * 0.25
    risk_score += 0.7 if len(prompt) > 2600 else 0.0
    risk_score += 0.35 if "HEALTH_PRIVACY_REVIEW" in findings else 0.0
    risk_score += 0.25 if "FINANCE_SIDE_EFFECT_REVIEW" in findings else 0.0
    risk_score = round(risk_score, 2)

    if risk_score <= 4.0 and not missing_prompt_apps:
        bucket = "A_likely_good_spot_check"
    elif risk_score <= 7.0:
        bucket = "B_close_verify_derivability"
    elif risk_score <= 10.0:
        bucket = "C_repair_candidate"
    else:
        bucket = "D_high_risk_manual_review"

    return {
        "key": row.get("key"),
        "env_id": row.get("env_id"),
        "data_id": row.get("data_id"),
        "version": row.get("version"),
        "data_version": row.get("data_version"),
        "current_date": env_vars.get("CURRENT_DATE"),
        "scenario": metadata.get("task_scenario_name"),
        "complexity_tier": metadata.get("task_complexity_tier"),
        "writer_timezone": metadata.get("writer_timezone") or "",
        "session_count": sessions.get("session_count", 0),
        "completed_sessions": sessions.get("completed_sessions", 0),
        "errored_sessions": sessions.get("errored_sessions", 0),
        "cancelled_sessions": sessions.get("cancelled_sessions", 0),
        "in_progress_sessions": sessions.get("in_progress_sessions", 0),
        "session_models": sessions.get("session_models", ""),
        "prompt_chars": len(prompt),
        "verifier_chars": len(verifier),
        "prompt_apps": "|".join(prompt_apps),
        "verifier_apps": "|".join(verifier_apps),
        "prompt_app_families": "|".join(prompt_app_families),
        "verifier_app_families": "|".join(verifier_app_families),
        "prompt_app_families_not_in_verifier": "|".join(missing_prompt_apps),
        "verifier_apps_not_in_prompt": "|".join(verifier_extra_apps),
        "verifier_no_change_guard_apps": "|".join(extra_no_change_guard_apps),
        "dependency_types": "|".join(dependencies),
        "dependency_count": len(dependencies),
        "relative_date_count": len(relative_dates),
        "relative_date_terms": "|".join(sorted(set(x.lower() for x in relative_dates))),
        "absolute_date_count": len(absolute_dates),
        "conditional_count": len(conditionals),
        "lookup_count": len(lookups),
        "money_literal_count": len(prompt_amounts),
        "verifier_only_amounts": "|".join(verifier_only_amounts),
        "verifier_only_user_values": " || ".join(verifier_only_literals),
        "findings": "|".join(findings),
        "risk_score": risk_score,
        "bucket": bucket,
        "prompt_preview": prompt_summary(prompt),
    }


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def read_json_or_cdp_body(path: Path) -> Any:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, dict) and "body" in payload:
        body = payload["body"]
        if isinstance(body, str):
            return json.loads(body)
    return payload


def load_session_stats(task_api_json: Path | None, sessions_json: Path | None) -> dict[str, dict[str, Any]]:
    if not task_api_json or not sessions_json:
        return {}
    task_rows = read_json_or_cdp_body(task_api_json)
    session_rows = read_json_or_cdp_body(sessions_json)
    id_to_key = {row.get("id"): row.get("key") for row in task_rows if row.get("id") and row.get("key")}

    per_key: dict[str, dict[str, Any]] = defaultdict(
        lambda: {
            "session_count": 0,
            "completed_sessions": 0,
            "errored_sessions": 0,
            "cancelled_sessions": 0,
            "in_progress_sessions": 0,
            "models": Counter(),
        }
    )
    for session in session_rows:
        key = id_to_key.get(session.get("eval_task"))
        if not key:
            continue
        stats = per_key[key]
        stats["session_count"] += 1
        status = session.get("status") or "unknown"
        if status == "completed":
            stats["completed_sessions"] += 1
        elif status == "errored":
            stats["errored_sessions"] += 1
        elif status == "cancelled":
            stats["cancelled_sessions"] += 1
        elif status == "in_progress":
            stats["in_progress_sessions"] += 1
        model = session.get("model")
        if model:
            stats["models"][model] += 1

    normalized: dict[str, dict[str, Any]] = {}
    for key, stats in per_key.items():
        normalized[key] = {
            "session_count": stats["session_count"],
            "completed_sessions": stats["completed_sessions"],
            "errored_sessions": stats["errored_sessions"],
            "cancelled_sessions": stats["cancelled_sessions"],
            "in_progress_sessions": stats["in_progress_sessions"],
            "session_models": "|".join(f"{model}:{count}" for model, count in stats["models"].most_common()),
        }
    return normalized


def markdown_table(rows: list[list[Any]], headers: list[str]) -> str:
    out = ["| " + " | ".join(headers) + " |"]
    out.append("| " + " | ".join(["---"] * len(headers)) + " |")
    for row in rows:
        escaped = [str(cell).replace("|", "\\|").replace("\n", " ") for cell in row]
        out.append("| " + " | ".join(escaped) + " |")
    return "\n".join(out)


def build_summary(scored: list[dict[str, Any]], scope_note: str = "") -> str:
    by_env = Counter(row["env_id"] for row in scored)
    by_bucket = Counter(row["bucket"] for row in scored)
    finding_counts = Counter(
        finding
        for row in scored
        for finding in str(row["findings"]).split("|")
        if finding
    )
    dependency_counts = Counter(
        dep
        for row in scored
        for dep in str(row["dependency_types"]).split("|")
        if dep
    )
    app_gap_counts = Counter(
        app
        for row in scored
        for app in str(row["prompt_app_families_not_in_verifier"]).split("|")
        if app
    )
    risk_scores = [float(row["risk_score"]) for row in scored]
    total_sessions = sum(int(row.get("session_count", 0) or 0) for row in scored)
    tasks_with_sessions = sum(1 for row in scored if int(row.get("session_count", 0) or 0) > 0)
    session_status_counts = {
        "completed": sum(int(row.get("completed_sessions", 0) or 0) for row in scored),
        "errored": sum(int(row.get("errored_sessions", 0) or 0) for row in scored),
        "cancelled": sum(int(row.get("cancelled_sessions", 0) or 0) for row in scored),
        "in_progress": sum(int(row.get("in_progress_sessions", 0) or 0) for row in scored),
    }
    model_counts = Counter()
    for row in scored:
        for part in str(row.get("session_models", "")).split("|"):
            if not part or ":" not in part:
                continue
            model, count = part.rsplit(":", 1)
            try:
                model_counts[model] += int(count)
            except ValueError:
                continue
    top_manual = sorted(scored, key=lambda r: (-float(r["risk_score"]), r["key"]))[:25]
    top_good = sorted(
        [r for r in scored if r["bucket"] == "A_likely_good_spot_check"],
        key=lambda r: (float(r["risk_score"]), r["key"]),
    )[:20]

    lines = [
        "# Project One Static QA Summary",
        "",
        "This report is a first-pass static triage over the exported JSONL dataset. It flags review leads; it does not replace environment inspection or human judgment.",
        "",
    ]
    if scope_note:
        lines.extend(
            [
                "## Scope",
                "",
                scope_note,
                "",
            ]
        )
    lines.extend(
        [
            "## Dataset Shape",
            "",
            f"- Tasks: {len(scored)}",
            f"- Risk score min/median/mean/max: {min(risk_scores):.2f} / {median(risk_scores):.2f} / {mean(risk_scores):.2f} / {max(risk_scores):.2f}",
            "",
            markdown_table([[k, v] for k, v in by_env.most_common()], ["Environment", "Tasks"]),
            "",
            "## Session Coverage",
            "",
            f"- Sessions joined to tasks: {total_sessions}",
            f"- Tasks with at least one session: {tasks_with_sessions}",
            "",
            markdown_table([[k, v] for k, v in session_status_counts.items()], ["Session status", "Sessions"]),
            "",
            markdown_table([[k, v] for k, v in model_counts.most_common()], ["Model", "Sessions"]),
            "",
            "## Static Buckets",
            "",
            markdown_table([[k, v] for k, v in by_bucket.most_common()], ["Bucket", "Tasks"]),
            "",
            "Bucket meanings:",
            "",
            "- `A_likely_good_spot_check`: low static risk; still needs sample environment verification.",
            "- `B_close_verify_derivability`: probably recoverable, but hidden dependencies or branching need checking.",
            "- `C_repair_candidate`: worth reviewing for repair, likely needs prompt/verifier/environment reconciliation.",
            "- `D_high_risk_manual_review`: highest-risk tasks by static signals; inspect before spending recovery time.",
            "",
            "## Most Common Findings",
            "",
            markdown_table([[k, v] for k, v in finding_counts.most_common(20)], ["Finding", "Tasks"]),
            "",
            "## Dependency Signals",
            "",
            markdown_table([[k, v] for k, v in dependency_counts.most_common(20)], ["Dependency", "Tasks"]),
            "",
            "## Prompt App Families Missing From Verifier Apps",
            "",
            markdown_table([[k, v] for k, v in app_gap_counts.most_common(20)], ["App cue", "Tasks"]),
            "",
            "## Highest-Priority Manual Review Queue",
            "",
            markdown_table(
                [
                    [
                        row["risk_score"],
                        row["bucket"],
                        row["env_id"],
                        row["key"],
                        row["findings"],
                        row["prompt_preview"],
                    ]
                    for row in top_manual
                ],
                ["Risk", "Bucket", "Env", "Task", "Findings", "Prompt preview"],
            ),
            "",
            "## Low-Risk Spot-Check Candidates",
            "",
            markdown_table(
                [
                    [
                        row["risk_score"],
                        row["env_id"],
                        row["key"],
                        row["dependency_types"],
                        row["prompt_preview"],
                    ]
                    for row in top_good
                ],
                ["Risk", "Env", "Task", "Dependencies", "Prompt preview"],
            ),
            "",
            "## How To Use This",
            "",
            "Start with the highest-priority queue to learn failure modes, then sample each bucket and environment. Promote tasks only after checking that prompt facts, verifier expectations, and world data reconcile.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_manual_queue(path: Path, scored: list[dict[str, Any]]) -> None:
    rows = sorted(scored, key=lambda r: (-float(r["risk_score"]), r["key"]))[:50]
    lines = [
        "# Manual Review Queue",
        "",
        "These are the top 50 tasks by static QA risk. Use this as a worklist, not as a rejection list.",
        "",
    ]
    for idx, row in enumerate(rows, 1):
        lines.extend(
            [
                f"## {idx}. {row['key']}",
                "",
                f"- Bucket: `{row['bucket']}`",
                f"- Risk score: `{row['risk_score']}`",
                f"- Environment: `{row['env_id']}`",
                f"- Findings: `{row['findings']}`",
                f"- Dependencies: `{row['dependency_types']}`",
                f"- Prompt apps: `{row['prompt_apps']}`",
                f"- Verifier apps: `{row['verifier_apps']}`",
                f"- Prompt app families missing from verifier: `{row['prompt_app_families_not_in_verifier']}`",
                f"- Verifier-only amounts: `{row['verifier_only_amounts']}`",
                f"- Verifier-only user values: `{row['verifier_only_user_values']}`",
                "",
                f"> {row['prompt_preview']}",
                "",
                "Manual check:",
                "",
                "- [ ] Open task world or session trace.",
                "- [ ] Verify each prompt lookup fact is present in seed data.",
                "- [ ] Verify verifier-only constants are derivable from seed data.",
                "- [ ] Decide: deliver as-is / small prompt fix / verifier fix / reject.",
                "",
            ]
        )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Static triage for Fleet Project One JSONL datasets.")
    parser.add_argument("dataset", type=Path, help="Path to exported dataset JSONL.")
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path("outputs/project_one_qa_tool/reports"),
        help="Directory for generated CSV/Markdown reports.",
    )
    parser.add_argument(
        "--task-api-json",
        type=Path,
        help="Optional task API JSON with task ids and keys for session joining.",
    )
    parser.add_argument(
        "--sessions-json",
        type=Path,
        help="Optional sessions API JSON, or a CDP Network.getResponseBody wrapper with a JSON body.",
    )
    parser.add_argument(
        "--require-sessions",
        action="store_true",
        help="Drop tasks with no visible sessions from generated outputs.",
    )
    args = parser.parse_args()

    rows = load_jsonl(args.dataset)
    session_stats = load_session_stats(args.task_api_json, args.sessions_json)
    all_scored = [score_task(row, session_stats) for row in rows]
    scored = all_scored
    scope_note = "Scope: all exported tasks."
    if args.require_sessions:
        scored = [
            row
            for row in all_scored
            if int(row.get("session_count", 0) or 0) > 0
        ]
        dropped_count = len(all_scored) - len(scored)
        scope_note = (
            "Scope: session-backed tasks only. Per Fleet guidance, tasks with no visible "
            f"sessions are dropped from this analysis for now. Included {len(scored)} "
            f"tasks and dropped {dropped_count} unrun tasks from the {len(all_scored)}-task export."
        )
    args.out_dir.mkdir(parents=True, exist_ok=True)

    write_csv(args.out_dir / "task_triage.csv", scored)
    (args.out_dir / "task_triage.json").write_text(
        json.dumps(scored, indent=2), encoding="utf-8"
    )
    (args.out_dir / "summary.md").write_text(
        build_summary(scored, scope_note), encoding="utf-8"
    )
    write_manual_queue(args.out_dir / "manual_review_queue.md", scored)

    print(f"Loaded {len(rows)} tasks")
    if args.require_sessions:
        print(f"Dropped {len(all_scored) - len(scored)} tasks without visible sessions")
        print(f"Scoped to {len(scored)} session-backed tasks")
    print(f"Wrote {args.out_dir / 'task_triage.csv'}")
    print(f"Wrote {args.out_dir / 'summary.md'}")
    print(f"Wrote {args.out_dir / 'manual_review_queue.md'}")


if __name__ == "__main__":
    main()
