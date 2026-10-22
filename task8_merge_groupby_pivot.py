import pandas as pd

orders = pd.read_csv("sales_dataset.csv")
orders["Units"] = orders["Units"].fillna(orders["Units"].median())
orders["CustomerRating"] = orders["CustomerRating"].fillna(orders["CustomerRating"].median())
orders["Sales"] = orders["Units"] * orders["UnitPrice"]

staff = pd.DataFrame({
    "Salesperson": ["Anil", "Sara", "Meena", "Ravi"],
    "ExperienceYears": [3, 4, 2, 5]
})
merged_df = pd.merge(orders, staff, on="Salesperson", how="left")
print("Merged data:")
print(merged_df[["OrderID", "Salesperson", "ExperienceYears", "Sales"]])

combined_df = pd.concat([orders.iloc[:6], orders.iloc[6:]], ignore_index=True)
print("\nConcatenated shape:", combined_df.shape)

region_summary = orders.groupby("Region").agg(
    TotalSales=("Sales", "sum"),
    AverageSales=("Sales", "mean"),
    OrderCount=("OrderID", "count"),
    MinimumSales=("Sales", "min"),
    MaximumSales=("Sales", "max")
).round(2)
print("\nRegion summary:")
print(region_summary)

pivot = pd.pivot_table(
    orders, values="Sales", index="Region", columns="Category",
    aggfunc="sum", fill_value=0
)
print("\nPivot table:")
print(pivot)
