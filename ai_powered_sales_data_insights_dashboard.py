# -*- coding: utf-8 -*-
"""AI-Powered Sales Data Insights Dashboard

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wSff_NohHSB2jnTT42sEbOAmmPAx27cw

# 📊 AI-Powered Sales Data Insights Report
**Created by: ABINAYA S**  
**Date: 13-07-2025**  
**Tools Used:** Python, Pandas, Matplotlib, Seaborn, AI

---

This report provides data-driven insights from company sales data across regions, products, and customer segments — built entirely with Python (no Power BI or Excel).  
It includes automated AI-style business summaries, sales trend analysis, and visual dashboards.
"""

import pandas as pd

# Try loading with encoding fix
df = pd.read_csv("/kaggle/sales_data_sample.csv", encoding='latin1')

# Preview first few rows
df.head()

"""## 📄 Executive Summary

- 🧠 This report analyzes over 2,800 historical sales transactions.
- 📈 Sales peaked in **Nov 2004**, and dipped in **Jan 2003**.
- 🌍 USA, France, and Germany lead in sales volume.
- 💼 Classic Cars, Vintage Cars, and Planes are top-selling product lines.
- 🧍‍♂️ Large deals generate the most revenue — ideal for high-value targeting.

These findings support strategic decisions in marketing, supply chain, and customer segmentation.

## 📂 Dataset Overview
(A quick look at the sales data used)
"""

# Convert ORDERDATE to datetime
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'], errors='coerce')

# Convert SALES to numeric just in case
df['SALES'] = pd.to_numeric(df['SALES'], errors='coerce')

# Drop rows with missing ORDERDATE or SALES
df.dropna(subset=['ORDERDATE', 'SALES'], inplace=True)

# Confirm the cleaned data
print("✅ Cleaned data shape:", df.shape)
df.info()

"""## 📆 Monthly Sales Trend
## 💼 Top Product Lines by Sales
Product line bar chart
"""

import matplotlib.pyplot as plt
import seaborn as sns

# Aggregate total sales by PRODUCTLINE
top_products = df.groupby('PRODUCTLINE')['SALES'].sum().sort_values(ascending=False)

# Plot
plt.figure(figsize=(10,6))
sns.barplot(x=top_products.values, y=top_products.index, palette='viridis')
plt.title("💼 Top Product Lines by Total Sales", fontsize=14)
plt.xlabel("Total Sales")
plt.ylabel("Product Line")
plt.tight_layout()
plt.show()

"""## 🌍 Country-wise Sales Distribution
(Pie chart showing top regions by sales)
"""

# Extract Year-Month for grouping
df['YEAR_MONTH'] = df['ORDERDATE'].dt.to_period('M')

# Group by Year-Month and sum SALES
monthly_sales = df.groupby('YEAR_MONTH')['SALES'].sum().reset_index()
monthly_sales['YEAR_MONTH'] = monthly_sales['YEAR_MONTH'].astype(str)  # Convert for plotting

# Plot
plt.figure(figsize=(12,6))
sns.lineplot(x='YEAR_MONTH', y='SALES', data=monthly_sales, marker='o', color='orange')
plt.xticks(rotation=45)
plt.title("📆 Monthly Sales Trend", fontsize=14)
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

"""## 🧍‍♂️ Deal Size Analysis
(Sales split by Small, Medium, Large deals)
"""

# Group sales by COUNTRY
country_sales = df.groupby('COUNTRY')['SALES'].sum().sort_values(ascending=False)

# Separate top 5 and group the rest as 'Others'
top_countries = country_sales.head(5)
others_total = country_sales[5:].sum()

# Combine using pd.concat
final_data = pd.concat([top_countries, pd.Series({'Others': others_total})])

# Plot
plt.figure(figsize=(8,8))
plt.pie(final_data, labels=final_data.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title("🌍 Sales Distribution by Country", fontsize=14)
plt.axis('equal')  # Keeps it a circle
plt.show()

"""## 🧍‍♂️ Deal Size Analysis
(Sales split by Small, Medium, Large deals)
"""

# Group by DEALSIZE and sum SALES
segment_sales = df.groupby('DEALSIZE')['SALES'].sum().sort_values(ascending=False)

# Plot
plt.figure(figsize=(8,5))
sns.barplot(x=segment_sales.index, y=segment_sales.values, palette='coolwarm')
plt.title("🧍‍♂️ Sales by Customer Segment (DEALSIZE)", fontsize=14)
plt.xlabel("Deal Size")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

"""## 🧠 AI-Generated Insights
(Smart summary generated using logic/AI)
"""

# Calculate key stats from monthly sales
peak_month = monthly_sales.loc[monthly_sales['SALES'].idxmax(), 'YEAR_MONTH']
low_month = monthly_sales.loc[monthly_sales['SALES'].idxmin(), 'YEAR_MONTH']
avg_sales = monthly_sales['SALES'].mean()

# Generate summary text
print("🧠 AI Insight Summary:")
print(f"- 📈 Sales peaked in {peak_month}, showing highest revenue during that period.")
print(f"- 📉 The lowest sales were recorded in {low_month}.")
print(f"- 📊 Average monthly sales were approximately ${avg_sales:,.2f}.")
print("- 💡 Consider investigating what drove performance in peak vs. low months.")