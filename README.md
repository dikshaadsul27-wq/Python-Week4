# Python-Week4
Sales Data Analysis Project
1. Project Overview and Objectives
This project analyzes sales transaction data to uncover business insights.
The dataset includes: Date, Product, Quantity, Price, Customer_ID, Region, and Total_Sales.
Objectives:
- Clean and preprocess the dataset (handle missing values).
- Compute key metrics such as total revenue, average order value, revenue by product/region, top customers, and monthly sales.
- Visualize insights using charts (line, bar, pie).
- Provide a structured report and reproducible code for stakeholders.

2. Setup and Installation Instructions
Prerequisites
- Python 3.10+
- Git installed locally
Installation Steps
- Clone the repository:
git clone https://github.com/your-username/sales-analysis.git
cd sales-analysis
- Install dependencies:
pip install -r requirements.txt
- Place your dataset (sales_data.csv) inside the data/ folder.
- Run the analysis:
python main.py


- or open analysis.ipynb in Jupyter Notebook.
3. Code Structure Explanation├── README.md              # Documentation
├── requirements.txt       # Dependencies (pandas, matplotlib)
├── main.py / analysis.ipynb  # Core analysis script
├── data/                  # Raw dataset
│   └── sales_data.csv
├── visualizations/        # Generated charts
│   ├── product_revenue.png
│   ├── region_revenue_pie.png
│   ├── top_customers.png
│   ├── monthly_sales.png
│   └── sales_over_time.png
└── report/                # Summary of insights
    └── report.md
- main.py: Loads data, cleans missing values, computes metrics, generates charts.
- visualizations/: Stores PNG charts created by Matplotlib.
- report/: Contains written insights and conclusions.
4. Screenshots of Working ApplicationScreenshots of generated charts (saved in visualizations/):
- sales_over_time.png → Line chart of daily sales trend.
- product_revenue.png → Bar chart of revenue by product.
- region_revenue_pie.png → Pie chart of revenue by region.
- top_customers.png → Bar chart of top 10 customers.
- monthly_sales.png → Line chart of monthly sales trend.

5. Explanation of How Technical Requirements Were Met- Data Cleaning: Missing values filled with column means (df.fillna(df.mean())).
- Metrics: Calculated total revenue (₹12,365,048.00), AOV, product/region revenue, top customers, monthly sales.
- Visualizations: Implemented multiple chart types (line, bar, pie) using Matplotlib.
- Reproducibility: Requirements listed in requirements.txt; dataset organized in data/; outputs saved in visualizations/.
- Documentation: README.md explains objectives, setup, structure, and results; report folder summarizes insights.
- Report: Highlights all insights, metrics, suggests business strategies and summaries the complete project
