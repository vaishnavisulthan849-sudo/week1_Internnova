import pandas as pd

df = pd.read_csv("sales_dataset.csv")
df["Sales"] = df["Units"] * df["UnitPrice"]

print("Selected columns:")
print(df[["OrderID", "Region", "Product", "Sales"]])
print("\nFirst three rows:")
print(df.iloc[0:3])
print("\nOrders with sales above 300:")
print(df[df["Sales"] > 300])
print("\nNorth region orders with at least 2 units:")
print(df[(df["Region"] == "North") & (df["Units"] >= 2)])
print("\nSales ascending:")
print(df.sort_values("Sales", ascending=True)[["OrderID", "Sales"]])
print("\nSales descending:")
print(df.sort_values("Sales", ascending=False)[["OrderID", "Sales"]])
