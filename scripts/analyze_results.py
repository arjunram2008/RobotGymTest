import pandas as pd

df = pd.read_csv("results/results.csv")

summary = df.groupby("experiment")["success"].agg(["sum", "count"])
summary["rate"] = summary["sum"] / summary["count"]

print(summary)
