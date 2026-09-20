import pandas as pd

# Load the main dataset
df = pd.read_csv("data/SuperKart.csv")

print("=" * 50)
print("SUPERKART DATASET OVERVIEW")
print("=" * 50)
print(f"Dataset Shape: {df.shape[0]} rows, {df.shape[1]} columns\n")

print("--- Column Summary & Missing Values ---")
summary_df = pd.DataFrame({
    "Data Type": df.dtypes,
    "Missing Values": df.isnull().sum(),
    "Missing %": (df.isnull().sum() / len(df)) * 100
})
print(summary_df)

print("\n--- Summary Statistics (Numerical Features) ---")
print(df.describe().T)

