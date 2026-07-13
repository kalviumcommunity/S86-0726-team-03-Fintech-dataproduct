import pandas as pd


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


if __name__ == "__main__":

    filepath = "data/raw/transactions.csv"

    df = ingest_csv(filepath)
    df = enforce_data_types(df)
    df = handle_missing_values(df)
    df = clean_string_columns(df)
    
    print("\nFirst 5 Rows:\n")
    print(df.head())
    profile_dataset(df)