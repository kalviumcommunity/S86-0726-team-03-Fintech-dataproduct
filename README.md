# Fintech Payment Recovery Analytics

## Project Overview

This project analyzes UPI payment transactions to help financial institutions understand payment failures, retry patterns, bank response codes, transaction behavior, and recovery opportunities. The goal is to distinguish between temporary payment failures and permanently lost revenue using data engineering and analytics techniques.

---

## Project Status

🚧 Data Engineering & Exploratory Data Analysis Completed

---

## Folder Structure

```
S86-0726-team-03-Fintech-dataproduct/
│── data/
│   ├── raw/
│   │   ├── transactions.csv
│   │   ├── payment_retries.csv
│   │   └── bank_response_codes.csv
│   └── processed/
│
│── dashboard/
│
│── notebooks/
│   └── data_exploration.ipynb
│
│── scripts/
│   ├── analyze_data.py
│   ├── clean_data.py
│   ├── validate_data.py
│   ├── distribution_analysis.py
│   ├── correlation_analysis.py
│   └── groupby_analysis.py
│
│── output/
│
│── README.md
│── requirements.txt
│── .gitignore
```

---

## Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- SQL
- Streamlit
- Plotly
- Git & GitHub

---

## Dataset

The project currently uses three datasets:

- **transactions.csv** – Main UPI transaction dataset
- **payment_retries.csv** – Retry information for failed transactions
- **bank_response_codes.csv** – Bank response code descriptions

---

## Data Engineering Pipeline

The project currently performs the following operations:

### Data Ingestion

- Load CSV datasets using Pandas
- Read and inspect transaction data

### Data Profiling

- Dataset shape
- Column information
- Data types
- Missing values
- Missing value percentage
- Duplicate detection
- Summary statistics
- Quality assessment

### Data Type Enforcement

- Convert Timestamp to datetime
- Convert Amount (INR) to numeric
- Extract:
  - Day
  - Month

### Missing Value Handling

- Numerical columns → Median imputation
- Categorical columns → Mode imputation
- Datetime columns → Forward Fill

### String Cleaning

- Remove extra spaces
- Convert text to lowercase
- Remove unwanted special characters
- Standardize transaction status values

### Outlier Detection

- Detect transaction amount outliers using the IQR method
- Flag outliers without removing records

### Data Validation

- Validate transaction amount
- Validate transaction status
- Validate Sender UPI IDs
- Validate Receiver UPI IDs
- Generate overall validation status for each record

### Data Integration

- Merge transactions dataset with payment retries dataset
- Merge transactions dataset with bank response codes dataset
- Create a unified dataset for analysis

### Distribution Analysis

- Histogram for transaction amount distribution
- Analyze transaction amount distribution
- Identify business trends through distribution

### Correlation Analysis

- Correlation matrix for numerical features
- Correlation heatmap visualization
- Analyze relationships between transaction amount, retry count, and response codes

### GroupBy Analysis

- Total transaction amount by status
- Transaction count by status
- Average transaction amount by status
- Average retry count by status

---

## Generated Features

The preprocessing pipeline generates the following business features:

- Day
- Month
- Retry Count
- Response Code
- Response Description
- Is_Outlier
- Valid_Amount
- Valid_Status
- Valid_Sender_UPI
- Valid_Receiver_UPI
- Passes_All_Checks

---

## Current Progress

- ✅ Repository setup
- ✅ Project folder structure
- ✅ Virtual environment setup
- ✅ Dependencies installed
- ✅ GitHub collaboration workflow
- ✅ Created transaction dataset
- ✅ Created payment retries dataset
- ✅ Created bank response codes dataset
- ✅ Dataset ingestion
- ✅ Dataset profiling
- ✅ Data type enforcement
- ✅ Missing value handling
- ✅ String cleaning & normalization
- ✅ Outlier detection
- ✅ Data validation rules
- ✅ Multi-source dataset merging
- ✅ Distribution analysis
- ✅ Correlation analysis
- ✅ Correlation heatmap visualization
- ✅ GroupBy analysis
- ✅ Transaction segmentation by status

---

## Upcoming Work

- Build an interactive Streamlit dashboard
- Create KPI cards
- Analyze payment retry trends
- Visualize bank response code distribution
- Build interactive business charts
- Generate business insights
- Deploy the application

---

## Team

**S86-0726 Team 03**

**Project:** Fintech Payment Recovery Analytics