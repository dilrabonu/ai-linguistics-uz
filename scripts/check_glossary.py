"""Validate glossary/glossary_en_uz.csv (run in CI)."""
import csv
import sys
from pathlib import Path

from uzling import normalize_uz

PATH = Path(__file__).resolve().parents[1] / "glossary" / "glossary_en_uz.csv"
COLUMNS = ["term_en", "term_uz", "definition_uz", "chapter", "status"]
STATUSES = {"proposed", "reviewed", "approved"}


def main() -> int:
    errors = []
    with PATH.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != COLUMNS:
            print(f"bad header: {reader.fieldnames}")
            return 1
        seen = set()
        for i, row in enumerate(reader, start=2):
            key = row["term_en"].strip().lower()
            if key in seen:
                errors.append(f"line {i}: duplicate term_en '{key}'")
            seen.add(key)
            if row["status"] not in STATUSES:
                errors.append(f"line {i}: status must be one of {sorted(STATUSES)}")
            if not row["chapter"].isdigit() or not 1 <= int(row["chapter"]) <= 14:
                errors.append(f"line {i}: chapter must be 1-14")
            for col in ("term_uz", "definition_uz"):
                if row[col] != normalize_uz(row[col]):
                    errors.append(f"line {i}: {col} is not normalized (run uzling.normalize_uz)")
    for e in errors:
        print(e)
    print(f"{len(seen)} terms checked, {len(errors)} problems")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
