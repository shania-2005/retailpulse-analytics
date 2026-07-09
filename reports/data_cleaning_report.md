# Data Cleaning Report

## Objective

The objective of data cleaning is to improve the quality of the Online Retail II dataset by removing inconsistent, duplicate, and invalid records before performing analysis.

---

## Dataset

- Dataset: Online Retail II
- Source: UCI Machine Learning Repository 
- Initial Records: 1,067,371
- Columns: 8

---

## Data Quality Issues Identified

### Missing Values

- Description contained a small number of missing values.
- Customer ID contained a large number of missing values.

### Duplicate Records

- Duplicate transactions were identified and removed.

### Invalid Quantity

- Transactions with Quantity ≤ 0 were removed.

### Invalid Price

- Transactions with Price ≤ 0 were removed.

### Cancelled Orders

- Cancelled invoices (Invoice starting with "C") were removed.

---

## Cleaning Steps Performed

- Removed missing Description values.
- Removed missing Customer ID values.
- Removed duplicate rows.
- Removed cancelled invoices.
- Removed transactions with invalid Quantity.
- Removed transactions with invalid Price.

---

## Output

The cleaned dataset was saved as:

data/interim/cleaned_data.csv

---

## Conclusion

The cleaned dataset is complete, consistent, and ready for exploratory data analysis and feature engineering.
