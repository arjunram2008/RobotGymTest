import csv
from collections import defaultdict

rows = []

with open("results/results.csv", newline="", encoding="utf-8") as file:
    for row in csv.DictReader(file):
        if row["success"] in {"0", "1"}:
            row["success"] = int(row["success"])
            rows.append(row)

if not rows:
    print("No completed tests yet.")
    raise SystemExit

groups = defaultdict(list)

for row in rows:
    groups[row["test"]].append(row["success"])

print(f"Completed tests: {len(rows)}")
print(f"Successful tests: {sum(row['success'] for row in rows)}/{len(rows)}")

for name, values in groups.items():
    print(f"{name}: {sum(values)}/{len(values)}")
