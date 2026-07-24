import pandas as pd
from validate_data import validate_data
from distribution_analysis import distribution_analysis
from correlation_analysis import correlation_analysis
from groupby_analysis import groupby_analysis
from funnel_analysis import funnel_analysis
from root_cause_analysis import root_cause_analysis
from failure_amount_distribution import failure_amount_distribution

from database import (
    save_to_database,
    load_from_database,
    check_database_schema
)

def ingest_csv(filepath, delimiter=",", encoding="utf-8"):
    """
    Load the CSV dataset.
    """
    df = pd.read_csv(filepath, delimiter=delimiter, encoding=encoding)
    return df


def profile_dataset(df):
    """
    Profile the dataset and print quality metrics.
    """

    print("=" * 50)
    print("DATASET PROFILING REPORT")
    print("=" * 50)

    # Dataset Shape
    print("\n1. Dataset Shape")
    print(df.shape)

    # Column Names
    print("\n2. Columns")
    print(df.columns.tolist())

    # Data Types
    print("\n3. Data Types")
    print(df.dtypes)

    # Missing Values
    print("\n4. Missing Values")
    print(df.isnull().sum())

    # Missing Value Percentage
    print("\n5. Missing Value Percentage")
    print((df.isnull().sum() / len(df) * 100).round(2))

    # Duplicate Rows
    print("\n6. Duplicate Rows")
    print(df.duplicated().sum())

    # Numerical Statistics
    print("\n7. Numerical Statistics")
    print(df.describe())

    # Status Distribution
    if "Status" in df.columns:
        print("\n8. Status Distribution")
        print(df["Status"].value_counts())

    # Simple Quality Assessment
    print("\n9. Quality Assessment")

    if df.isnull().sum().sum() == 0:
        print("✔ No missing values found.")
    else:
        print("⚠ Missing values detected.")

    if df.duplicated().sum() == 0:
        print("✔ No duplicate rows found.")
    else:
        print(f"⚠ {df.duplicated().sum()} duplicate rows found.")

    print("\nProfiling completed successfully!")

def handle_missing_values(df):
    """
    Detect and handle missing values using different strategies.
    """

    print("=" * 50)
    print("MISSING VALUE DETECTION & IMPUTATION")
    print("=" * 50)

    print("\nMissing Values Before Imputation:")
    print(df.isnull().sum())

    # Loop through every column
    for column in df.columns:

        # Skip if there are no missing values
        if df[column].isnull().sum() == 0:
            continue

        print(f"\nHandling missing values in '{column}'")

        # ---------- Numerical Columns ----------
        if pd.api.types.is_numeric_dtype(df[column]):

            median = df[column].median()
            df[column] = df[column].fillna(median)

            print(f"Filled numerical column '{column}' with median ({median})")

        # ---------- Datetime Columns ----------
        elif pd.api.types.is_datetime64_any_dtype(df[column]):

            df[column] = df[column].ffill()

            print(f"Forward filled datetime column '{column}'")

        # ---------- Categorical / Object Columns ----------
        else:

            mode = df[column].mode()

            if not mode.empty:
                df[column] = df[column].fillna(mode[0])

                print(f"Filled categorical column '{column}' with mode ({mode[0]})")

            else:
                print(f"Could not determine mode for '{column}'")

    print("\nMissing Values After Imputation:")
    print(df.isnull().sum())

    return df

def enforce_data_types(df):
    """
    Convert columns to appropriate data types.
    """

    print("=" * 50)
    print("DATA TYPE ENFORCEMENT")
    print("=" * 50)

    # Convert Timestamp to datetime
    df["Timestamp"] = pd.to_datetime(
        df["Timestamp"],
        format="%Y-%m-%d %H:%M:%S"
    )

    # Ensure Amount is numeric
    df["Amount (INR)"] = pd.to_numeric(
        df["Amount (INR)"],
        errors="coerce"
    )

    print("\nData Types After Conversion:\n")
    print(df.dtypes)

    return df

import re

def clean_text_column(series, lowercase=True, strip=True, remove_special=False, mapping=None):
    """
    Clean a text column.
    """

    result = series.copy()

    if strip:
        result = result.str.strip()

    if lowercase:
        result = result.str.lower()

    if remove_special:
        result = result.str.replace(r'[^a-zA-Z0-9 ]', '', regex=True)

    if mapping:
        result = result.replace(mapping)

    return result

def clean_string_columns(df):

    print("=" * 50)
    print("STRING CLEANING & TEXT NORMALIZATION")
    print("=" * 50)

    status_map = {
        "success": "SUCCESS",
        "failed": "FAILED",
        "pending": "PENDING"
    }

    # Sender Name
    df["Sender Name"] = clean_text_column(
        df["Sender Name"],
        lowercase=True,
        strip=True,
        remove_special=True
    )

    # Receiver Name
    df["Receiver Name"] = clean_text_column(
        df["Receiver Name"],
        lowercase=True,
        strip=True,
        remove_special=True
    )

    # Sender UPI ID
    df["Sender UPI ID"] = clean_text_column(
        df["Sender UPI ID"],
        lowercase=True,
        strip=True
    )

    # Receiver UPI ID
    df["Receiver UPI ID"] = clean_text_column(
        df["Receiver UPI ID"],
        lowercase=True,
        strip=True
    )

    # Status
    df["Status"] = clean_text_column(
        df["Status"],
        lowercase=True,
        strip=True
    )

    df["Status"] = df["Status"].replace(status_map)

    print("\nString cleaning completed successfully.\n")

    return df

def detect_outliers(df):
    """
    Detect outliers in Amount (INR) using the IQR method.
    """

    print("=" * 50)
    print("OUTLIER DETECTION")
    print("=" * 50)

    Q1 = df["Amount (INR)"].quantile(0.25)
    Q3 = df["Amount (INR)"].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Create a new column to flag outliers
    df["Is_Outlier"] = (
        (df["Amount (INR)"] < lower_bound) |
        (df["Amount (INR)"] > upper_bound)
    )

    print(f"Lower Bound : {lower_bound:.2f}")
    print(f"Upper Bound : {upper_bound:.2f}")
    print(f"Outliers Found : {df['Is_Outlier'].sum()}")

    return df

def run_sql_metric(query_file):
    """
    Read and execute a SQL business metric query.
    """

    from sqlalchemy import create_engine

    engine = create_engine("sqlite:///analytics.db")

    with open(query_file, "r", encoding="utf-8") as file:
        query = file.read()

    result = pd.read_sql(query, engine)
    
    return result

def create_sql_view(query_file):
    """
    Create a reusable SQL view in the database.
    """

    from sqlalchemy import create_engine

    engine = create_engine("sqlite:///analytics.db")

    with open(query_file, "r", encoding="utf-8") as file:
        query = file.read()

    with engine.begin() as connection:
        connection.exec_driver_sql(query)

    print(f"SQL view created successfully: {query_file}")


if __name__ == "__main__":

    transactions = ingest_csv("data/raw/transactions.csv")
    payment_retries = ingest_csv("data/raw/payment_retries.csv")
    bank_responses = ingest_csv("data/raw/bank_response_codes.csv")

    transactions = enforce_data_types(transactions)
    transactions = handle_missing_values(transactions)
    transactions = clean_string_columns(transactions)
    transactions = detect_outliers(transactions)
    transactions = validate_data(transactions)

 # ==========================================
    # CLEAN PAYMENT RETRIES
    # ==========================================

    payment_retries["Retry Count"] = pd.to_numeric(
        payment_retries["Retry Count"],
        errors="coerce"
    )

    payment_retries["Retry Count"] = payment_retries[
        "Retry Count"
    ].fillna(0)

    # ==========================================
    # CLEAN BANK RESPONSE CODES
    # ==========================================

    bank_responses["Response Code"] = (
        bank_responses["Response Code"]
        .astype(str)
        .str.strip()
    )

    bank_responses["Response Description"] = (
        bank_responses["Response Description"]
        .astype(str)
        .str.strip()
    )

    # ==========================================
    # SAVE ALL CLEANED TABLES TO DATABASE
    # ==========================================

    save_to_database(
        transactions,
        payment_retries,
        bank_responses
    )
    # ==========================================
    # CREATE SQL VIEWS 
     # ==========================================

    create_sql_view(
    "queries/views/vw_failure_analysis.sql"
    )
    
    create_sql_view(
        "queries/views/vw_revenue_by_status.sql"
    )
    
    create_sql_view(
        "queries/views/vw_transaction_summary.sql"
    )


    # ==========================================
    # CHECK DATABASE SCHEMA
    # ==========================================

    check_database_schema()


    # ==========================================
    # LOAD DATA BACK FROM DATABASE
    # ==========================================

    df_from_sql = load_from_database()

    # Convert Timestamp back to datetime
    # SQLite may load it as a string
    df_from_sql["Timestamp"] = pd.to_datetime(
        df_from_sql["Timestamp"],
        errors="coerce"
    )
    
    # ==========================================
    # SQL BUSINESS METRICS
    # ==========================================

    print("\n" + "=" * 50)
    print("SQL BUSINESS METRICS")
    print("=" * 50)

    # Metric 1: Transaction Summary
    transaction_summary = run_sql_metric(
        "queries/transaction_summary.sql"
    )

    print("\nTransaction Summary:")
    print(transaction_summary)


    # Metric 2: Revenue by Status
    revenue_by_status = run_sql_metric(
        "queries/revenue_by_status.sql"
    )

    print("\nRevenue by Status:")
    print(revenue_by_status)


    # Metric 3: Failure Reasons
    failure_reasons = run_sql_metric(
        "queries/failure_reasons.sql"
    )

    print("\nFailure Reasons:")
    print(failure_reasons)

    # Metr1c 4: Top Customers
    top_customers = run_sql_metric(
    "queries/top_customers.sql"
    )

    print("\nTop Customers:")
    print(top_customers)

    #Metric - Optimized Failure Analysis
    optimized_failure_analysis = run_sql_metric(
    "queries/optimized_failure_analysis.sql"
    )

    print("\nOptimized Failure Analysis:")
    print(optimized_failure_analysis)

    # Metric 5: Joining the tables
    joined_data = run_sql_metric(
    "queries/join_tables.sql"
    
    )
    print("\n" + "=" * 60)
    print("3-TABLE JOIN RESULT")
    print("=" * 60)

    print(joined_data.head())


    print("\nFirst 5 Rows Loaded From SQL Database:\n")
    print(df_from_sql.head())


    # ==========================================
    # RUN ANALYSIS USING DATA FROM DATABASE
    # ==========================================

    profile_dataset(df_from_sql)

    distribution_analysis(df_from_sql)

    correlation_analysis(df_from_sql)

    groupby_analysis(df_from_sql)

    funnel_analysis(df_from_sql)

    root_cause_analysis(df_from_sql)

    failure_amount_distribution(df_from_sql)

    