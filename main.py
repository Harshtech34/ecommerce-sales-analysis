import pandas as pd
import matplotlib.pyplot as plt
import os

# -------------------------------
# Load Data
# -------------------------------
try:
    df = pd.read_csv("data/sales_data.csv")
except FileNotFoundError:
    print("Error: Dataset not found.")
    exit()

# -------------------------------
# Data Cleaning
# -------------------------------
df.dropna(inplace=True)
df['Date'] = pd.to_datetime(df['Date'])
df['Total_Sales'] = df['Quantity'] * df['Price']

# -------------------------------
# Analysis
# -------------------------------
total_revenue = df['Total_Sales'].sum()
average_order_value = df['Total_Sales'].mean()

product_sales = df.groupby('Product')['Total_Sales'].sum()
monthly_sales = df.groupby(df['Date'].dt.month)['Total_Sales'].sum()

print("Total Revenue:", total_revenue)
print("Average Order Value:", average_order_value)

# -------------------------------
# Visualization
# -------------------------------
os.makedirs("visualizations", exist_ok=True)

# Line Chart - Monthly Sales
plt.figure()
monthly_sales.plot()
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales Trend")
plt.savefig("visualizations/monthly_sales_trend.png")
plt.close()

# Bar Chart - Product Sales
plt.figure()
product_sales.plot(kind='bar')
plt.xlabel("Product")
plt.ylabel("Sales")
plt.title("Product-wise Sales Distribution")
plt.savefig("visualizations/product_sales_distribution.png")
plt.close()

print("Analysis completed successfully.")
