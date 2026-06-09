import pandas as pd
import matplotlib.pyplot as plt

# ==========================
# Load Dataset
# ==========================
df = pd.read_csv(
    "data/Sample - Superstore.csv",
    encoding="latin1"
)

# ==========================
# Basic Information
# ==========================
print("Dataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nData Types:")
print(df.dtypes)

print("\nSummary Statistics:")
print(df.describe())

print("\nUnique Values:")
print(df.nunique())

# ==========================
# Convert Date Column
# ==========================
df["Order Date"] = pd.to_datetime(df["Order Date"])

# ==========================
# Monthly Sales Trend
# ==========================
monthly_sales = df.groupby(
    df["Order Date"].dt.to_period("M")
)["Sales"].sum()

monthly_sales.index = monthly_sales.index.to_timestamp()

plt.figure(figsize=(12, 6))
plt.plot(monthly_sales.index, monthly_sales.values)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)

plt.savefig("screenshots/monthly_sales_trend.png")
plt.show()

# ==========================
# Region Wise Sales
# ==========================
region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(8, 5))
region_sales.plot(kind="bar")
plt.title("Region Wise Sales")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.grid(True)

plt.savefig("screenshots/region_sales.png")
plt.show()

# ==========================
# Category Wise Sales
# ==========================
category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8, 5))
category_sales.plot(kind="bar")
plt.title("Category Wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.grid(True)

plt.savefig("screenshots/category_sales.png")
plt.show()

# ==========================
# Profit By Category
# ==========================
category_profit = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(8, 5))
category_profit.plot(kind="bar")
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.grid(True)

plt.savefig("screenshots/profit_by_category.png")
plt.show()

print("\nAnalysis Completed Successfully!")