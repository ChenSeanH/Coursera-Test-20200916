import pandas as pd
import json, pathlib, sys

# Paths ?? need to change the csv file name
CSV_IN = pathlib.Path("data/raw.csv")
JSON_OUT = pathlib.Path("public/data.json")

def main():
    # 1) Read CSV
    if not CSV_IN.exists():
        sys.exit(f"[ERROR] Missing input CSV: {CSV_IN} (put your data there or change the path)")
    df = pd.read_csv(CSV_IN)

    # 2) Minimal schema for the demo (change columns as you like)
    needed = ["Age", "Parent_Satisfaction_Score"]
    missing = [c for c in needed if c not in df.columns]
    if missing:
        sys.exit(f"[ERROR] Missing required columns: {missing}. Present columns: {list(df.columns)}")

    # 3) Build records for D3
    records = df[["Age", "Parent_Satisfaction_Score"]].to_dict(orient="records")

    # 4) Write JSON
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.write_text(json.dumps(records, indent=2), encoding="utf-8")
    print(f"[OK] Wrote {JSON_OUT} with {len(records)} records")

if __name__ == "__main__":
    main()
