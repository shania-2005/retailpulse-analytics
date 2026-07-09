# 🛍️ RetailPulse: Online Retail Sales Analysis

RetailPulse is an end-to-end Data Analytics project built using the Online Retail II dataset. The project focuses on cleaning retail transaction data, performing exploratory data analysis (EDA), engineering meaningful features, validating data quality, and generating business insights that support data-driven decision making.

---

## 📌 Project Objective

The objective of this project is to analyze customer purchasing behavior and identify valuable business insights by answering questions such as:

- Which products generate the highest sales?
- Who are the top customers?
- Which countries contribute the most revenue?
- What are the monthly and yearly sales trends?
- How do quantity and price influence revenue?

---

## 📂 Project Structure

```text
RetailPulse/
│
├── config/
│
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_exploratory_data_analysis.ipynb
│   ├── 04_feature_engineering.ipynb
│   └── 05_data_validation.ipynb
│
├── outputs/
│   └── figures/
│
├── reports/
│   ├── data_cleaning_report.md
│   └── eda_report.md
│
├── src/
│   ├── data/
│   ├── features/
│   ├── visualization/
│   └── utils/
│
├── main.py
├── requirements.txt
└── README.md
```

---

# 📊 Dataset

**Dataset:** Online Retail II

**Source:** UCI Machine Learning Repository / Kaggle

The dataset contains transactional records from an online retail store, including invoice details, customer information, products, quantities, prices, and countries.

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- VS Code
- Git & GitHub

---

# 🧹 Data Cleaning

The following cleaning steps were performed:

- Removed missing Description values
- Removed missing Customer ID values
- Removed duplicate records
- Removed cancelled invoices
- Removed transactions with Quantity ≤ 0
- Removed transactions with Price ≤ 0

---

# 📈 Exploratory Data Analysis

The project includes:

- Year-wise Transaction Analysis
- Monthly Transaction Trend
- Day of Week Analysis
- Hourly Sales Analysis
- Top 10 Products by Quantity
- Top 10 Products by Revenue
- Top 10 Customers
- Customer Purchase Frequency
- Country-wise Revenue Analysis
- Unit Price Distribution
- Purchase Quantity Distribution
- Basket-size Analysis
- Correlation Heatmap
- Outlier Detection

---

# ⚙️ Feature Engineering

The following features were created:

- Revenue
- Year
- Month
- Month Number
- Day
- Day of week
- Hour
- Year_Month
- Quarter
- Basket-size
- Isweekend
- Order-value


---

# ✅ Data Validation

Validation checks include:

- Missing Values
- Duplicate Records
- Invalid Quantity
- Invalid Price
- Data Types

---

# 💡 Key Business Insights
- Sales transactions increased steadily from 2009 to 2011, indicating business growth.
- Monthly sales peaked during October and November, suggesting strong seasonal demand.
- The United Kingdom contributed the highest revenue, making it the primary market.
- A few customers generated a significant share of the total revenue, highlighting high-value customers.
- Certain products consistently achieved high sales volumes and revenue, making them top-performing products.
- Most transactions involved small purchase quantities (especially 1, 2, 6, and 12 units).
- The majority of product prices were below 5, while a small number of premium-priced items created price outliers.
- Quantity showed a strong positive correlation with Revenue (≈ 0.83), indicating that larger purchases generally produced higher revenue.
- Price had only a weak positive correlation with Revenue (≈ 0.14), suggesting that sales volume influenced revenue more than unit price.
- Thursday generated the highest revenue among all weekdays.
- Sales activity was concentrated during business hours, with peak transactions occurring during the daytime.
- Quantity and Price contained outliers, but these records were retained because they represented genuine business transactions rather than data errors.

---

# 📷 Project Outputs

The project generates:

- Cleaned Dataset
- Feature Engineered Dataset
- EDA Visualizations
- Business Reports

---

# 🚀 Future Improvements

- SQL Business Analysis
- Interactive Power BI Dashboard
- Customer Segmentation
- RFM Analysis
- Sales Forecasting
- Streamlit Web Application

---

# 👩‍💻 Author

**Shania Shamshi**

BCA Student | Data Analytics

GitHub:
https://github.com/shania-2005

---
