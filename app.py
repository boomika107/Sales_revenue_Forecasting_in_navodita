import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 

# Page Title
st.title("Sales and Revenue Forecasting Dashboard")

# Load Data
df = pd.read_csv("data/Sample - Superstore.csv", encoding="latin1")

# Convert Date
df["Order Date"] = pd.to_datetime(df["Order Date"])

# KPIs
st.subheader("Business Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Sales", f"${df['Sales'].sum():,.2f}")

with col2:
    st.metric("Total Profit", f"${df['Profit'].sum():,.2f}")

with col3:
    st.metric("Total Orders", f"{df['Order ID'].nunique()}")

# Monthly Sales Trend
st.subheader("Monthly Sales Trend")

monthly_sales = df.groupby(
    df["Order Date"].dt.to_period("M")
)["Sales"].sum()

monthly_sales.index = monthly_sales.index.to_timestamp()

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(monthly_sales.index, monthly_sales.values)
ax.set_title("Monthly Sales Trend")
ax.set_xlabel("Month")
ax.set_ylabel("Sales")

st.pyplot(fig)

# Region Wise Sales
st.subheader("Region Wise Sales")

region_sales = df.groupby("Region")["Sales"].sum()

fig2, ax2 = plt.subplots(figsize=(8, 5))
region_sales.plot(kind="bar", ax=ax2)
ax2.set_title("Region Wise Sales")

st.pyplot(fig2)

# Category Wise Sales
st.subheader("Category Wise Sales")

category_sales = df.groupby("Category")["Sales"].sum()

fig3, ax3 = plt.subplots(figsize=(8, 5))
category_sales.plot(kind="bar", ax=ax3)
ax3.set_title("Category Wise Sales")

st.pyplot(fig3)
# ==========================
# Future Sales Forecast
# ==========================

import joblib

st.subheader("Future Sales Forecast")

# Load trained model
model = joblib.load("models/sales_forecast.pkl")

# Generate next 6 months
future_months = pd.DataFrame({
    "Month_Number": range(48, 54)
})

future_predictions = model.predict(future_months)

forecast_df = pd.DataFrame({
    "Month": [f"Month {i}" for i in range(1, 7)],
    "Predicted Sales": future_predictions
})

st.dataframe(forecast_df)

st.line_chart(
    forecast_df.set_index("Month")
)