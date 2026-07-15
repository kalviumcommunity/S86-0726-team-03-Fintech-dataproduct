# Fintech Payment Recovery Analytics

## Project Overview

This project analyzes UPI payment transactions to help financial institutions understand payment failures, retry patterns, bank response codes, transaction behavior, and recovery opportunities. The goal is to distinguish between temporary payment failures and permanently lost revenue using data engineering and analytics techniques.

---

## Project Status

🚧 Data Cleaning & Exploration Phase Completed

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
│   └── distribution_analysis.py
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
- Duplicate detection
- Summary statistics
- Quality assessment

### Data Type Enforcement
- Convert Timestamp to datetime
- Convert Amount to numeric
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
- Detect transaction amount outliers using IQR
- Flag outliers without removing records

### Data Validation
- Validate transaction amount
- Validate transaction status
- Validate Sender UPI IDs
- Validate Receiver UPI IDs
- Overall validation status

### Distribution Analysis
- Histogram for transaction amount distribution
- Basic business trend visualization

---

## Current Progress

- ✅ Repository setup
- ✅ Project folder structure
- ✅ Virtual environment setup
- ✅ Dependencies installed
- ✅ GitHub collaboration workflow
- ✅ Dataset ingestion
- ✅ Dataset profiling
- ✅ Data type enforcement
- ✅ Missing value handling
- ✅ String cleaning & normalization
- ✅ Outlier detection
- ✅ Data validation rules
- ✅ Distribution analysis
- ✅ Created payment retries dataset
- ✅ Created bank response codes dataset

---

## Team

S86-0726 Team 03

Project: **Fintech Payment Recovery Analytics**