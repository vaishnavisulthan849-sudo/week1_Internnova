import pandas as pd

df = pd.read_csv("sales_dataset.csv")
print("Missing values by column:")
print(df.isna().sum())

dropped_df = df.dropna()
print("\nRows after dropping records with any missing values:", len(dropped_df))

clean_df = df.copy()
clean_df["Units"] = clean_df["Units"].fillna(clean_df["Units"].median())
clean_df["CustomerRating"] = clean_df["CustomerRating"].fillna(
    clean_df["CustomerRating"].median()
)
print("\nMissing values after filling:")
print(clean_df.isna().sum())
print("\nCleaned dataset:")
print(clean_df)
