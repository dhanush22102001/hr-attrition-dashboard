"""HR Attrition analysis — standard library only.
Reads data/hr_attrition_sample.csv and prints the metrics used in the dashboard:
overall attrition, attrition by department, by tenure band, and top exit reasons.
Dataset is fictional and created for portfolio demonstration."""

import csv
from collections import defaultdict
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data" / "hr_attrition_sample.csv"


def pct(part, whole):
    return round(part / whole * 100, 1) if whole else 0.0


def main():
    rows = list(csv.DictReader(open(DATA)))
    total = len(rows)
    left = [r for r in rows if r["attrition"] == "Yes"]
    print(f"Employees analysed: {total}")
    print(f"Employees who left: {len(left)}")
    print(f"Overall attrition rate: {pct(len(left), total)}%\n")

    print("Attrition by department:")
    depts = defaultdict(list)
    for r in rows:
        depts[r["department"]].append(r)
    for dept, sub in sorted(depts.items(), key=lambda kv: -pct(sum(x['attrition'] == 'Yes' for x in kv[1]), len(kv[1]))):
        l = sum(x["attrition"] == "Yes" for x in sub)
        print(f"  {dept:<18} {l:>3}/{len(sub):<3}  {pct(l, len(sub))}%")

    print("\nAttrition by tenure band:")
    bands = {"0-2 yrs": lambda t: t < 2, "2-5 yrs": lambda t: 2 <= t < 5, "5+ yrs": lambda t: t >= 5}
    for label, fn in bands.items():
        sub = [r for r in rows if fn(float(r["tenure_years"]))]
        l = sum(x["attrition"] == "Yes" for x in sub)
        print(f"  {label:<8} {l:>3}/{len(sub):<3}  {pct(l, len(sub))}%")

    print("\nTop exit reasons:")
    reasons = defaultdict(int)
    for r in left:
        if r["exit_reason"]:
            reasons[r["exit_reason"]] += 1
    for reason, count in sorted(reasons.items(), key=lambda kv: -kv[1]):
        print(f"  {reason:<20} {count}")


if __name__ == "__main__":
    main()
