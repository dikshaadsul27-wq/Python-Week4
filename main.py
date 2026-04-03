import pandas as pd
df = pd.read_csv("sales_data.csv")

print(df.info())
print(df.isnull().sum())

df_filled = df.fillna(df.mean(numeric_only=True))

# Total revenue
total_revenue = df_filled['Total_Sales'].sum()
print(f"Total Revenue: ₹{total_revenue:,.2f}")

# Revenue by product
product_revenue = df_filled.groupby("Product")["Total_Sales"].sum()
top_products = product_revenue.sort_values(ascending=False)

# Best product
best_product = top_products.index[0]
best_revenue = top_products.iloc[0]
print(f"Best product: {best_product} with revenue ₹{best_revenue:,.2f}")

# --- METRICS ---

# Total Revenue
total_revenue = df['Total_Sales'].sum()
print(f"Total Revenue: ₹{total_revenue:,.2f}")

# Average Order Value (AOV)
aov = df['Total_Sales'].mean()
print(f"Average Order Value: ₹{aov:,.2f}")

# Revenue by Product
product_revenue = df.groupby("Product")["Total_Sales"].sum()

# Revenue by Region
region_revenue = df.groupby("Region")["Total_Sales"].sum()

# Top Customers
top_customers = df.groupby("Customer_ID")["Total_Sales"].sum().sort_values(ascending=False).head(10)

# Monthly Sales
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby("Month")["Total_Sales"].sum()

# --- CHARTS ---

import matplotlib.pyplot as plt

# 1. Line chart: Sales trend over time
plt.figure(figsize=(10,6))
plt.plot(df['Date'], df['Total_Sales'], marker='o', linestyle='-', color='blue')
plt.title("Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Sales (₹)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Bar chart: Revenue by Product
product_revenue.sort_values().plot(kind="bar", color="skyblue")
plt.title("Revenue by Product")
plt.ylabel("Revenue (₹)")
plt.xlabel("Product")
plt.tight_layout()
plt.show()

# 3. Pie chart: Revenue by Region
region_revenue.plot(kind="pie", autopct="%1.1f%%", startangle=90, colormap="Set3")
plt.title("Revenue by Region")
plt.ylabel("")
plt.tight_layout()
plt.show()

# 4. Bar chart: Top 10 Customers
top_customers.plot(kind="bar", color="orange")
plt.title("Top 10 Customers by Revenue")
plt.ylabel("Revenue (₹)")
plt.xlabel("Customer ID")
plt.tight_layout()
plt.show()

# 5. Line chart: Monthly Sales
monthly_sales.plot(kind="line", marker='o', color="green")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales (₹)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


