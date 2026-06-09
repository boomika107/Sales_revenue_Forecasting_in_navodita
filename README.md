# 📈 Sales and Revenue Forecasting Dashboard

## 🚀 Project Overview

The Sales and Revenue Forecasting Dashboard is a Data Analytics and Machine Learning project developed using Python, Pandas, Scikit-Learn, and Streamlit. The project analyzes historical sales data, visualizes business insights, and forecasts future sales trends to support data-driven business decisions.

## 🎯 Problem Statement

Businesses often face challenges in predicting future sales and revenue due to changing customer demand, seasonal fluctuations, and market trends. Accurate forecasting is essential for inventory management, resource planning, and strategic decision-making. This project aims to analyze historical sales data and predict future sales using Machine Learning techniques.

## 🎯 Objectives

* Analyze historical sales data.
* Perform data cleaning and preprocessing.
* Identify sales and revenue trends.
* Analyze performance across regions and categories.
* Build a Machine Learning forecasting model.
* Predict future sales trends.
* Develop an interactive Streamlit dashboard.

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-Learn
* Streamlit
* Joblib

## 📂 Dataset

**Dataset Used:** Sample Superstore Dataset

Dataset Features:

* Order Information
* Customer Information
* Product Information
* Sales
* Quantity
* Discount
* Profit
* Region and Category Details

## 📊 Features

### Data Analysis

* Missing Value Analysis
* Duplicate Data Check
* Statistical Summary
* Sales Trend Analysis

### Data Visualization

* Monthly Sales Trend
* Region-wise Sales Analysis
* Category-wise Sales Analysis
* Profit Analysis

### Machine Learning

* Linear Regression Model
* Future Sales Forecasting
* Model Persistence using Joblib

### Dashboard

* Total Sales KPI
* Total Profit KPI
* Total Orders KPI
* Interactive Charts
* Future Sales Predictions

## 🏗️ Project Architecture

Dataset (CSV)

↓

Data Preprocessing

↓

Exploratory Data Analysis (EDA)

↓

Machine Learning Model (Linear Regression)

↓

Sales Forecasting

↓

Streamlit Dashboard

↓

Business Insights & Predictions

## 📁 Project Structure

```text
Sales_revenue_Forecasting_in_navodita/
│
├── data/
│   └── Sample - Superstore.csv
│
├── models/
│   └── sales_forecast.pkl
│
├── screenshots/
│   ├── monthly_sales_trend.png
│   ├── region_sales.png
│   ├── category_sales.png
│   └── profit_by_category.png
│
├── app.py
├── train_model.py
├── forecast_model.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone <repository-url>
cd Sales_revenue_Forecasting_in_navodita
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Running the Project

Train the model:

```bash
python forecast_model.py
```

Run the dashboard:

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

## 📈 Forecast Results

The model forecasts future sales for the upcoming months based on historical sales trends using Linear Regression.

Example Forecast:

| Month   | Predicted Sales |
| ------- | --------------- |
| Month 1 | $69,957         |
| Month 2 | $70,859         |
| Month 3 | $71,761         |
| Month 4 | $72,663         |
| Month 5 | $73,565         |
| Month 6 | $74,467         |

## 🔮 Future Enhancements

* Advanced Forecasting Models (ARIMA, Prophet)
* Real-time Data Integration
* Cloud Deployment
* Downloadable Reports
* Enhanced Dashboard Filters
* Interactive Forecast Controls

## 👩‍💻 Author

**Boomika Kathirvel**

Aspiring Data Analyst | AI & Machine Learning Enthusiast

## ⭐ Project Outcome

This project demonstrates practical skills in:

* Data Analytics
* Data Visualization
* Machine Learning
* Forecasting Techniques
* Dashboard Development
* Business Intelligence

It serves as a complete end-to-end Data Analytics and Machine Learning portfolio project.
