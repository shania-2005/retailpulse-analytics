# RetailPulse - Retail Analytics using Machine Learning & Deep Learning

## Project Overview

RetailPulse is a Machine Learning and Deep Learning based retail analytics project designed to help retail businesses analyze customer behavior and improve business decisions.

The project includes:

- Customer Segmentation
- Customer Churn Prediction
- Demand Forecasting
- Deep Learning (LSTM)
- Model Comparison
- Hyperparameter Tuning

---

## Project Objectives

- Segment customers based on purchasing behavior.
- Predict customers who are likely to leave (Churn Prediction).
- Forecast future product demand.
- Compare multiple Machine Learning models.
- Tune the best model using GridSearchCV.
- Save final trained models for deployment.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- TensorFlow / Keras
- Google Colab
- VS Code

---

## Project Structure

```
RetailPulse Project
│
├── Notebooks
│   ├── 06_customer_segmentation.ipynb
│   ├── 07_churn_prediction.ipynb
│   ├── 08_demand_forecasting.ipynb
│   ├── 09_model_comparison.ipynb
│   ├── 10_Demand_forecasting.ipynb
│   └── 11_hyperparameter_tuning.ipynb
│
├── Model Files
│   ├── customer_segmentation.pkl
│   ├── churn_model.pkl
│   ├── best_churn_model.pkl
│   ├── forecast_model.pkl
│   └── lstm_demand_forecasting.keras
│
├── CSV Report Files
│   ├── customer_segmentation.csv
│   ├── customer_churn_prediction.csv
│   ├── forecast_predictions.csv
│   ├── lstm_predictions.csv
│   ├── model_comparison.csv
│   └── hyperparameter_report.csv
│
└── README.md
```

---

# Modules

## 1. Customer Segmentation

- Algorithm: K-Means Clustering
- Output:
  - Customer Groups
  - customer_segmentation.csv
  - customer_segmentation.pkl

---

## 2. Customer Churn Prediction

- Algorithm: Random Forest Classifier
- Output:
  - Customer Churn Prediction
  - customer_churn_prediction.csv
  - churn_model.pkl

---

## 3. Demand Forecasting

Two forecasting approaches were implemented:

### Machine Learning Forecasting

- Forecast future demand
- forecast_predictions.csv
- forecast_model.pkl

### Deep Learning Forecasting

- LSTM Neural Network
- lstm_predictions.csv
- lstm_demand_forecasting.keras

---

## 4. Model Comparison

Different Machine Learning algorithms were compared based on their performance metrics.

Output:

- model_comparison.csv

---

## 5. Hyperparameter Tuning

GridSearchCV was used to optimize the Random Forest model.

Best Parameters:

- max_depth = 3
- min_samples_split = 2
- n_estimators = 50

Best Accuracy:

- 1.00

Output:

- hyperparameter_report.csv
- best_churn_model.pkl

---

# Best Models

| Task                  | Best Model    |
| --------------------- | ------------- |
| Customer Segmentation | K-Means       |
| Churn Prediction      | Random Forest |
| Demand Forecasting    | LSTM          |

---

# Final Trained Models

- customer_segmentation.pkl
- churn_model.pkl
- best_churn_model.pkl
- forecast_model.pkl
- lstm_demand_forecasting.keras

---

# Performance Reports

The project generates:

- Customer Segmentation Report
- Churn Prediction Report
- Forecast Prediction Report
- LSTM Prediction Report
- Model Comparison Report
- Hyperparameter Tuning Report

---

# Author

**Nitesh Kumar Mishra**

Master of Computer Applications (MCA)

RetailPulse Project
