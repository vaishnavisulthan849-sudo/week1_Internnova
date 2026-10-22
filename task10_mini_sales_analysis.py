import numpy as np
import pandas as pd

df = pd.read_csv("sales_dataset.csv")
print("Original shape:", df.shape)
print("Missing values before cleaning:")
print(df.isna().sum())

df["Units"] = df["Units"].fillna(df["Units"].median())
df["CustomerRating"] = df["CustomerRating"].fillna(df["CustomerRating"].median())
df["Sales"] = df["Units"] * df["UnitPrice"]

print("\nOrders with sales of at least 300:")
print(df[df["Sales"] >= 300][["OrderID", "Region", "Product", "Sales"]])

print("\nTop orders by sales:")
print(df.sort_values("Sales", ascending=False)[["OrderID", "Product", "Sales"]].head())

region_analysis = df.groupby("Region").agg(
    TotalSales=("Sales", "sum"),
    AverageSales=("Sales", "mean"),
    NumberOfOrders=("OrderID", "count")
).round(2)
print("\nRegion analysis:")
print(region_analysis)

product_analysis = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
print("\nTotal sales by product:")
print(product_analysis)

pivot = pd.pivot_table(df, values="Sales", index="Region", columns="Category",
                       aggfunc="sum", fill_value=0)
print("\nPivot table:")
print(pivot)

values = df["Sales"].to_numpy()
print("\nTotal sales:", round(np.sum(values), 2))
print("Average order sales:", round(np.mean(values), 2))
print("Median order sales:", round(np.median(values), 2))
print("Highest order sales:", round(np.max(values), 2))

df.to_csv("final_sales_analysis.csv", index=False)
print("\nExported final_sales_analysis.csv")
