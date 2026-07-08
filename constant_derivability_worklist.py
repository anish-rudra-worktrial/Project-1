#!/usr/bin/env python3
"""Build a human-review worklist for verifier constants.

This is the second QA layer for Project One. The static triage script tells us
which tasks look risky; this script extracts the concrete verifier constants
that a reviewer should prove against seed data before promoting a task.
"""

from __future__ import annotations

import argparse
import ast
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


MONEY_PATTERN = re.compile(r"\$\s?\d[\d,]*(?:\.\d{1,2})?")
MONEY_NUMERIC_PATTERN = re.compile(r"(?<![\w.])\d{1,6}\.\d{1,2}(?![\w.])")
EMAIL_PATTERN = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)
PHONE_PATTERN = re.compile(r"\b(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]\d{3}[-.\s]\d{4}\b")
DATE_PATTERN = re.compile(
    r"\b(?:\d{1,2}/\d{1,2}(?:/\d{2,4})?|\d{4}-\d{2}-\d{2}|"
    r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*\.?\s+\d{1,2}"
    r"(?:,\s*\d{4})?)\b",
    re.IGNORECASE,
)


APP_HINTS = [
    ("meridian", ["meridian", "credit card", "statement", "autopay", "pay over time", "rewards"]),
    ("harbor", ["harbor", "checking", "savings", "zelle", "bank", "transfer"]),
    ("ledger", ["quickbooks", "ledger", "invoice", "bill", "vendor", "customer", "contractor"]),
    ("medora", ["medora", "doctor", "dentist", "provider", "appointment", "visit", "reservation"]),
    ("lifeline", ["lifeline", "prescription", "medication", "patient", "insurance", "pcp"]),
    ("communications", ["outlook", "latch", "email", "calendar", "inbox", "message", "task list"]),
]


STRING_NOISE_PARTS = {
    "ERROR_ACCUMULATOR",
    "SUCCESS_ACCUMULATOR",
    "TASK_FAILED_SCORE",
    "TASK_SUCCESSFUL_SCORE",
    "created_at",
    "updated_at",
    "sqlite_sequence",
    "expected",
    "actual",
    "database",
    "Combined verifier",
    "individual app verifiers",
}


STRING_NOISE_PATTERNS = [
    re.compile(pattern, re.IGNORECASE)
    for pattern in [
        r"\bgot\b",
        r"\bexpected\b",
        r"\bactual\b",
        r"\bverify\b",
        r"\bvalidate\b",
        r"\bverified\b",
        r"\bscore\b",
        r"\brow\b",
        r"\bcount\b",
        r"\bfound\b",
        r"\bcontains\b",
        r"\bcorrect\b",
        r"\bmissing\b",
        r"\bcreated\b",
        r"\bupdated\b",
        r"\bdatabase\b",
        r"\brollback\b",
        r"\bsuccessful\b",
        r"\bfailed\b",
        r"\berror\b",
        r"\bguard\b",
        r"\bapp\s+\w+",
        r"sqlite",
        r"^['\",;:.()\-\s]+$",
        r"^\{.*\}$",
        r"^\[.*\]$",
    ]
]


PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}
BUCKET_ORDER = {
    "D_high_risk_manual_review": 0,
    "C_repair_candidate": 1,
    "B_close_verify_derivability": 2,
    "A_likely_good_spot_check": 3,
}
TYPE_ORDER = {"money": 0, "date": 1, "email": 2, "phone": 3, "name_or_label": 4}


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def load_triage(path: Path | None) -> dict[str, dict[str, str]]:
    if not path:
        return {}
    with path.open("r", encoding="utf-8", newline="") as f:
        return {row["key"]: row for row in csv.DictReader(f)}


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        return
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def normalize_space(value: str) -> str:
    return " ".join(value.strip().split())


def normalize_amount(value: str) -> str:
    stripped = value.replace("$", "").replace(",", "").replace(" ", "")
    try:
        number = float(stripped)
    except ValueError:
        return stripped
    return f"{number:.2f}".rstrip("0").rstrip(".")


def prompt_preview(prompt: str, limit: int = 190) -> str:
    squashed = normalize_space(prompt)
    return squashed if len(squashed) <= limit else squashed[: limit - 3] + "..."


def line_context(lines: list[str], line_number: int, radius: int = 1, limit: int = 220) -> str:
    if line_number <= 0:
        return ""
    start = max(0, line_number - 1 - radius)
    end = min(len(lines), line_number + radius)
    context = normalize_space(" ".join(lines[start:end]))
    return context if len(context) <= limit else context[: limit - 3] + "..."


def money_values(text: str) -> set[str]:
    values = {normalize_amount(match.group(0)) for match in MONEY_PATTERN.finditer(text)}
    for match in MONEY_NUMERIC_PATTERN.finditer(text):
        try:
            number = float(match.group(0))
        except ValueError:
            continue
        if 5 <= number <= 250000:
            values.add(normalize_amount(match.group(0)))
    return values


def prompt_mentions(prompt: str, constant_type: str, constant: str) -> bool:
    prompt_lower = prompt.lower()
    if constant_type == "money":
        return normalize_amount(constant) in money_values(prompt)
    return constant.lower() in prompt_lower


def looks_like_user_value(value: str) -> bool:
    if EMAIL_PATTERN.search(value) or PHONE_PATTERN.search(value) or DATE_PATTERN.search(value):
        return True
    if re.search(
        r"\b\d{2,5}\s+[A-Z][A-Za-z0-9'.-]+\s+"
        r"(?:St|Street|Ave|Avenue|Rd|Road|Ln|Lane|Way|Blvd|Drive|Dr)\b",
        value,
    ):
        return True
    title_words = re.findall(r"\b[A-Z][a-z]+(?:'[a-z]+)?\b", value)
    if len(title_words) >= 2:
        return True
    label_words = re.findall(r"[A-Za-z][A-Za-z'&.-]+", value)
    acronym_words = re.findall(r"\b[A-Z]{2,}\b", value)
    return len(label_words) >= 2 and len(acronym_words) >= 1 and any(
        word[0].isupper() for word in label_words
    )


def clean_string_literal(value: str) -> str | None:
    cleaned = normalize_space(value).strip("%")
    if len(cleaned) < 5 or len(cleaned) > 180:
        return None
    if "[X]" in cleaned or "[C]" in cleaned:
        return None
    if "{" in cleaned or "}" in cleaned:
        return None
    if any(part in cleaned for part in ["!=", "==", "<", ">", " id=", " ids=", "bill_id=", "appointment_id"]):
        return None
    if any(char in cleaned for char in ["(", ")"]):
        return None
    lower = cleaned.lower()
    if lower.startswith(
        (
            "is ",
            "are ",
            "has ",
            "does ",
            "not ",
            "new ",
            "should ",
            "matches ",
            "match ",
            "debug ",
            "info ",
            "replace ",
        )
    ):
        return None
    if re.search(
        r"\b(should|matches?|doesn|fallback|debug|info|amount|total|balance|payment_date|"
        r"transaction|record|records|created|updated|computed|correctly)\b",
        lower,
    ):
        return None
    if len(re.findall(r"[A-Za-z][A-Za-z'&.-]+", cleaned)) > 10:
        return None
    if any(part in cleaned for part in STRING_NOISE_PARTS):
        return None
    if cleaned.count("_") >= 2:
        return None
    if re.fullmatch(r"[a-z_]+", cleaned):
        return None
    if any(pattern.search(cleaned) for pattern in STRING_NOISE_PATTERNS):
        return None
    return cleaned


def classify_string_constant(value: str) -> str | None:
    if EMAIL_PATTERN.fullmatch(value):
        return "email"
    if PHONE_PATTERN.fullmatch(value):
        return "phone"
    if DATE_PATTERN.fullmatch(value):
        return "date"
    if looks_like_user_value(value):
        return "name_or_label"
    return None


def add_constant(
    constants: dict[tuple[str, str], dict[str, Any]],
    constant_type: str,
    constant: str,
    context: str,
    line_number: int,
) -> None:
    if constant_type == "money":
        canonical = normalize_amount(constant)
    else:
        canonical = normalize_space(constant)
    if not canonical:
        return
    key = (constant_type, canonical.lower())
    record = constants.setdefault(
        key,
        {
            "constant_type": constant_type,
            "constant": canonical,
            "contexts": [],
            "line_numbers": [],
            "occurrence_count": 0,
        },
    )
    record["occurrence_count"] += 1
    if context and context not in record["contexts"] and len(record["contexts"]) < 3:
        record["contexts"].append(context)
    if line_number and line_number not in record["line_numbers"] and len(record["line_numbers"]) < 5:
        record["line_numbers"].append(line_number)


def extract_constants(verifier: str) -> list[dict[str, Any]]:
    constants: dict[tuple[str, str], dict[str, Any]] = {}
    lines = verifier.splitlines()

    for line_number, line in enumerate(lines, 1):
        context = line_context(lines, line_number)
        for match in MONEY_PATTERN.finditer(line):
            add_constant(constants, "money", match.group(0), context, line_number)
        for match in MONEY_NUMERIC_PATTERN.finditer(line):
            try:
                number = float(match.group(0))
            except ValueError:
                continue
            if 5 <= number <= 250000:
                add_constant(constants, "money", match.group(0), context, line_number)
        for match in DATE_PATTERN.finditer(line):
            add_constant(constants, "date", match.group(0), context, line_number)
        for match in EMAIL_PATTERN.finditer(line):
            add_constant(constants, "email", match.group(0), context, line_number)
        for match in PHONE_PATTERN.finditer(line):
            add_constant(constants, "phone", match.group(0), context, line_number)

    try:
        tree = ast.parse(verifier)
    except SyntaxError:
        tree = None

    if tree is not None:
        for node in ast.walk(tree):
            if not isinstance(node, ast.Constant) or not isinstance(node.value, str):
                continue
            cleaned = clean_string_literal(node.value)
            if not cleaned:
                continue
            line_number = getattr(node, "lineno", 0)
            context = line_context(lines, line_number)
            for match in DATE_PATTERN.finditer(cleaned):
                add_constant(constants, "date", match.group(0), context, line_number)
            for match in EMAIL_PATTERN.finditer(cleaned):
                add_constant(constants, "email", match.group(0), context, line_number)
            for match in PHONE_PATTERN.finditer(cleaned):
                add_constant(constants, "phone", match.group(0), context, line_number)
            constant_type = classify_string_constant(cleaned)
            if constant_type:
                add_constant(constants, constant_type, cleaned, context, line_number)

    return list(constants.values())


def likely_source_app(prompt: str, context: str, env_id: str, constant_type: str) -> str:
    context_lower = context.lower()
    prompt_lower = prompt.lower()

    if "health" in env_id:
        billing_hints = ["bill", "billing", "balance", "guarantor", "patient", "lifeline", "prescription"]
        appointment_hints = ["appointment", "provider", "doctor", "dentist", "visit", "medora"]
        if constant_type == "money" and any(
            hint in context_lower or hint in prompt_lower for hint in billing_hints
        ):
            return "lifeline"
        if any(
            hint in context_lower for hint in billing_hints
        ):
            return "lifeline"
        if any(
            hint in context_lower for hint in appointment_hints
        ):
            return "medora"
        if any(
            hint in prompt_lower for hint in appointment_hints
        ):
            return "medora"
        if any(hint in prompt_lower for hint in billing_hints):
            return "lifeline"

    for app, hints in APP_HINTS:
        if any(hint in context_lower for hint in hints):
            return app

    for app, hints in APP_HINTS:
        if any(hint in prompt_lower for hint in hints):
            return app

    if "health" in env_id:
        return "health_seed_data"
    if "finance" in env_id:
        return "finance_seed_data"
    return "unknown_seed_data"


def derivability_question(constant_type: str, constant: str, source_app: str) -> str:
    if constant_type == "money":
        if source_app == "meridian":
            return "Can this card amount be uniquely derived from Meridian statement/card data under the prompt filters?"
        if source_app == "harbor":
            return "Can this banking amount be uniquely derived from Harbor transactions, balances, or transfer rules?"
        if source_app == "ledger":
            return "Can this invoice/bill amount be uniquely derived from Ledger or QuickBooks records?"
        if source_app == "lifeline":
            return "Can this health billing amount be uniquely derived from Lifeline records?"
        return "Can this amount be uniquely derived from seed data rather than being verifier-only ground truth?"
    if constant_type == "date":
        return "Is this date/time implied by the prompt, current-date anchor, calendar, or source record?"
    if constant_type in {"email", "phone"}:
        return "Is this contact detail uniquely selected by the prompt and source records?"
    if source_app == "medora":
        return "Is this provider, clinic, or appointment uniquely selected by the prompt constraints?"
    if source_app == "communications":
        return "Is this email/calendar/task value uniquely selected by the prompt search criteria?"
    if source_app == "ledger":
        return "Is this vendor, customer, invoice, or bill value uniquely selected by the prompt constraints?"
    return "Can this user-visible value be derived from prompt plus seed data, or is it an ungrounded verifier constant?"


def review_priority(bucket: str, constant_type: str, mentioned: bool) -> str:
    if mentioned:
        return "low"
    if bucket in {"D_high_risk_manual_review", "C_repair_candidate"}:
        return "high"
    if constant_type in {"money", "date", "name_or_label"}:
        return "high"
    return "medium"


def build_worklist(
    dataset_rows: list[dict[str, Any]],
    triage_rows: dict[str, dict[str, str]],
    include_prompt_mentioned: bool,
) -> list[dict[str, Any]]:
    worklist: list[dict[str, Any]] = []
    for row in dataset_rows:
        task_key = row.get("key") or ""
        prompt = row.get("prompt") or ""
        verifier = row.get("verifier_func") or ""
        env_id = row.get("env_id") or ""
        triage = triage_rows.get(task_key, {})
        bucket = triage.get("bucket", "unbucketed")
        risk_score = triage.get("risk_score", "")
        session_count = triage.get("session_count", "")

        for constant in extract_constants(verifier):
            mentioned = prompt_mentions(prompt, constant["constant_type"], constant["constant"])
            if mentioned and not include_prompt_mentioned:
                continue
            context = " || ".join(constant["contexts"])
            source_app = likely_source_app(prompt, context, env_id, constant["constant_type"])
            priority = review_priority(bucket, constant["constant_type"], mentioned)
            worklist.append(
                {
                    "task_key": task_key,
                    "env_id": env_id,
                    "bucket": bucket,
                    "risk_score": risk_score,
                    "session_count": session_count,
                    "review_priority": priority,
                    "constant_type": constant["constant_type"],
                    "constant": constant["constant"],
                    "prompt_mentions_constant": str(mentioned),
                    "likely_source_app": source_app,
                    "occurrence_count": constant["occurrence_count"],
                    "verifier_line_numbers": "|".join(str(n) for n in constant["line_numbers"]),
                    "verifier_context": context,
                    "derivability_question": derivability_question(
                        constant["constant_type"], constant["constant"], source_app
                    ),
                    "prompt_preview": prompt_preview(prompt),
                }
            )

    return sorted(
        worklist,
        key=lambda r: (
            PRIORITY_ORDER.get(r["review_priority"], 99),
            BUCKET_ORDER.get(r["bucket"], 99),
            TYPE_ORDER.get(r["constant_type"], 99),
            -int(r["occurrence_count"]),
            r["task_key"],
            r["constant"],
        ),
    )


def markdown_table(rows: list[list[Any]], headers: list[str]) -> str:
    out = ["| " + " | ".join(headers) + " |"]
    out.append("| " + " | ".join(["---"] * len(headers)) + " |")
    for row in rows:
        escaped = [str(cell).replace("|", "\\|").replace("\n", " ") for cell in row]
        out.append("| " + " | ".join(escaped) + " |")
    return "\n".join(out)


def build_summary(worklist: list[dict[str, Any]], task_count: int) -> str:
    priority_counts = Counter(row["review_priority"] for row in worklist)
    type_counts = Counter(row["constant_type"] for row in worklist)
    app_counts = Counter(row["likely_source_app"] for row in worklist)
    bucket_counts = Counter(row["bucket"] for row in worklist)
    task_counts = Counter(row["task_key"] for row in worklist)

    top_rows = worklist[:40]
    top_tasks = [
        [
            count,
            next(row["bucket"] for row in worklist if row["task_key"] == task_key),
            task_key,
        ]
        for task_key, count in task_counts.most_common(20)
    ]

    lines = [
        "# Constant Derivability Worklist",
        "",
        "This is a second QA layer on top of the static triage. It extracts verifier constants that are not obviously present in the prompt and turns them into a review queue.",
        "",
        "A row here is not automatically a bug. It is a concrete question for a human reviewer: can this verifier value be uniquely derived from the prompt and seed world?",
        "",
        "## Shape",
        "",
        f"- Tasks scanned: {task_count}",
        f"- Constants requiring review: {len(worklist)}",
        f"- Tasks represented: {len(task_counts)}",
        "",
        markdown_table([[k, v] for k, v in priority_counts.most_common()], ["Priority", "Rows"]),
        "",
        markdown_table([[k, v] for k, v in type_counts.most_common()], ["Constant type", "Rows"]),
        "",
        markdown_table([[k, v] for k, v in app_counts.most_common()], ["Likely source app", "Rows"]),
        "",
        markdown_table([[k, v] for k, v in bucket_counts.most_common()], ["Task bucket", "Rows"]),
        "",
        "## Tasks With The Most Constants To Prove",
        "",
        markdown_table(top_tasks, ["Constants", "Bucket", "Task"]),
        "",
        "## Highest-Priority Rows",
        "",
        markdown_table(
            [
                [
                    row["review_priority"],
                    row["bucket"],
                    row["constant_type"],
                    row["likely_source_app"],
                    row["constant"],
                    row["task_key"],
                    row["derivability_question"],
                ]
                for row in top_rows
            ],
            ["Priority", "Bucket", "Type", "Source app", "Constant", "Task", "Question"],
        ),
        "",
        "## How To Use This",
        "",
        "1. Open `derivability_worklist.csv` and filter to `review_priority=high`.",
        "2. For each row, inspect the prompt, verifier context, and seed/session evidence.",
        "3. Mark the constant as explicitly prompted, uniquely derivable, ambiguous, or not derivable.",
        "4. Promote the task only when every verifier constant used for success is grounded.",
        "",
        "## Limits",
        "",
        "- This is still static analysis; it does not open seed databases or recordings.",
        "- The likely source app is heuristic, especially for cross-app tasks.",
        "- Some constants are valid no-change guards or implementation details despite looking user-visible.",
        "- The best next step is to connect these rows to seed-data probes for the highest-volume apps.",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract verifier constants that need derivability review."
    )
    parser.add_argument("dataset", type=Path, help="Path to exported dataset JSONL.")
    parser.add_argument(
        "--triage-csv",
        type=Path,
        help="Optional task_triage.csv from triage_dataset.py for bucket/session fields.",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path("outputs/project_one_qa_tool/reports"),
        help="Directory for generated worklist files.",
    )
    parser.add_argument(
        "--include-prompt-mentioned",
        action="store_true",
        help="Also include constants already mentioned verbatim in the prompt.",
    )
    args = parser.parse_args()

    dataset_rows = load_jsonl(args.dataset)
    triage_rows = load_triage(args.triage_csv)
    worklist = build_worklist(dataset_rows, triage_rows, args.include_prompt_mentioned)
    args.out_dir.mkdir(parents=True, exist_ok=True)

    write_csv(args.out_dir / "derivability_worklist.csv", worklist)
    (args.out_dir / "derivability_worklist.json").write_text(
        json.dumps(worklist, indent=2), encoding="utf-8"
    )
    (args.out_dir / "derivability_summary.md").write_text(
        build_summary(worklist, len(dataset_rows)), encoding="utf-8"
    )

    print(f"Loaded {len(dataset_rows)} tasks")
    print(f"Wrote {len(worklist)} derivability rows")
    print(f"Wrote {args.out_dir / 'derivability_worklist.csv'}")
    print(f"Wrote {args.out_dir / 'derivability_summary.md'}")


if __name__ == "__main__":
    main()
