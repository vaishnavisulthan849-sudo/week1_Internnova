import pandas as pd

df = pd.read_csv("sales_dataset.csv")
df["Units"] = df["Units"].fillna(df["Units"].median())
df["CustomerRating"] = df["CustomerRating"].fillna(df["CustomerRating"].median())
df["Sales"] = df["Units"] * df["UnitPrice"]

output_file = "processed_sales_dataset.csv"
df.to_csv(output_file, index=False)
print("Processed data exported to:", output_file)

verified_df = pd.read_csv(output_file)
print("\nFirst five exported rows:")
print(verified_df.head())
print("\nExported shape:", verified_df.shape)
print("\nMissing values:")
print(verified_df.isna().sum())
