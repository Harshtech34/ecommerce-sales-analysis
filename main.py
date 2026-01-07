import pandas as pd
import matplotlib.pyplot as plt
import os

# -------------------------------
# Load Dataset
# -------------------------------
try:
    df = pd.read_csv("data/sales_data.csv")
except FileNotFoundError:
    print("Dataset file not found.")
    exit()

# -------------------------------
# Data Cleaning
# -------------------------------

# Remove duplicate header rows
df = df[df['Date'] != 'Date']

# Convert data types
df['Date'] = pd.to_datetime(df['Date'])
df['Quantity'] = pd.to_numeric(df['Quantity'])
df['Price'] = pd.to_numeric(df['Price'])

# Recalculate Total Sales for validation
df['Calculated_Total_Sales'] = df['Quantity'] * df['Price']

# Replace incorrect Total_Sales if needed
df['Total_Sales'] = df['Calculated_Total_Sales']

# -------------------------------
# Basic Analysis
# -------------------------------
total_revenue = df['Total_Sales'].sum()
average_order_value = df['Total_Sales'].mean()

product_sales = df.groupby('Product')['Total_Sales'].sum()
region_sales = df.groupby('Region')['Total_Sales'].sum()
daily_sales = df.groupby('Date')['Total_Sales'].sum()

print("Total Revenue:", total_revenue)
print("Average Order Value:", average_order_value)

# -------------------------------
# Visualization
# -------------------------------
os.makedirs("visualizations", exist_ok=True)

# Chart 1: Product-wise Sales (Bar Chart)
plt.figure()
product_sales.plot(kind='bar')
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.title("Product-wise Sales Distribution")
plt.savefig("visualizations/product_sales_distribution.png")
plt.close()

# Chart 2: Daily Sales Trend (Line Chart)
plt.figure()
daily_sales.plot()
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.title("Daily Sales Trend")
plt.savefig("visualizations/daily_sales_trend.png")
plt.close()

print("Analysis and visualization completed successfully.")
