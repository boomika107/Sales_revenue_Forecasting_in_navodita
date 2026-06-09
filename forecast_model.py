import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import joblib

# Load dataset
df = pd.read_csv("data/Sample - Superstore.csv", encoding="latin1")

# Convert date
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Monthly sales
monthly_sales = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
    .sum()
    .reset_index()
)

monthly_sales["Month_Number"] = range(len(monthly_sales))

# Features and target
X = monthly_sales[["Month_Number"]]
y = monthly_sales["Sales"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Accuracy
predictions = model.predict(X)
score = r2_score(y, predictions)

print("Model Accuracy (R² Score):", round(score, 4))

# Predict next 6 months
future_months = pd.DataFrame({
    "Month_Number": range(
        len(monthly_sales),
        len(monthly_sales) + 6
    )
})

future_predictions = model.predict(future_months)

print("\nForecast for Next 6 Months:")

for i, value in enumerate(future_predictions, start=1):
    print(f"Month {i}: ${value:.2f}")

# Save model
joblib.dump(model, "models/sales_forecast.pkl")

print("\nModel saved successfully!")