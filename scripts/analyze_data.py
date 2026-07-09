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


if __name__ == "__main__":

    filepath = "data/raw/transactions.csv"

    df = ingest_csv(filepath)
    df = enforce_data_types(df)
    
    print("\nFirst 5 Rows:\n")
    print(df.head())
    profile_dataset(df)