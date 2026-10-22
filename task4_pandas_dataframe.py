import pandas as pd

scores = pd.Series([82, 91, 76, 88], name="Marks")
print("Pandas Series:")
print(scores)

data = {
    "Name": ["Asha", "Ravi", "Meena", "Kiran"],
    "Branch": ["CSE", "ECE", "CSE", "IT"],
    "Marks": [82, 91, 76, 88]
}
df = pd.DataFrame(data)
print("\nOriginal DataFrame:")
print(df)
print("\nColumn names:", df.columns.tolist())
print("Index:", df.index.tolist())

df["Result"] = df["Marks"].apply(lambda mark: "Pass" if mark >= 40 else "Fail")
print("\nUpdated DataFrame:")
print(df)
