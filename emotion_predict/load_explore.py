import pandas as pd
import os

# ── 1. Load ──────────────────────────────────────────────────────────────────
DATA_PATH = r"C:\Users\sayee\OneDrive\Desktop\emotion_predict\Sample_arvyax_reflective_dataset.xlsx"
df = pd.read_excel(DATA_PATH)

print("=" * 55)
print("DATASET LOADED")
print("=" * 55)
print(f"Shape : {df.shape[0]} rows × {df.shape[1]} columns")
print(f"Memory: {df.memory_usage(deep=True).sum() / 1024:.1f} KB\n")

# ── 2. Column overview ───────────────────────────────────────────────────────
print("COLUMNS & DTYPES")
print("-" * 40)
print(df.dtypes.to_string())

# ── 3. First look ────────────────────────────────────────────────────────────
print("\nFIRST 5 ROWS")
print("-" * 40)
print(df.head().to_string())

# ── 4. Missing values ────────────────────────────────────────────────────────
print("\nMISSING VALUES")
print("-" * 40)
null_counts = df.isnull().sum()
null_pct    = (null_counts / len(df) * 100).round(2)
missing = pd.DataFrame({"count": null_counts, "pct_%": null_pct})
missing = missing[missing["count"] > 0]
if missing.empty:
    print("  ✅ No missing values found.")
else:
    print(missing.to_string())

# ── 5. Duplicates ────────────────────────────────────────────────────────────
print(f"\nDUPLICATE ROWS : {df.duplicated().sum()}")

# ── 6. Numeric summary ───────────────────────────────────────────────────────
num_cols = df.select_dtypes(include="number").columns.tolist()
print(f"\nNUMERIC SUMMARY  ({num_cols})")
print("-" * 40)
print(df[num_cols].describe().round(2).to_string())

# ── 7. Categorical unique values ─────────────────────────────────────────────
cat_cols = df.select_dtypes(include="object").columns.drop("journal_text", errors="ignore")
print("\nCATEGORICAL COLUMNS — VALUE COUNTS")
print("-" * 40)
for col in cat_cols:
    print(f"\n▸ {col}  ({df[col].nunique()} unique):")
    print(df[col].value_counts().to_string())

print("\n✅ Exploration complete.")
