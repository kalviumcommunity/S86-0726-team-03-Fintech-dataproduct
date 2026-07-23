import pandas as pd
from sqlalchemy import create_engine, inspect


# Create SQLite database connection
DATABASE_URL = "sqlite:///analytics.db"

engine = create_engine(DATABASE_URL)


def save_to_database(df, payment_retries, bank_responses):

    df.to_sql(
        "transactions_cleaned",
        engine,
        if_exists="replace",
        index=False
    )

    payment_retries.to_sql(
        "payment_retries",
        engine,
        if_exists="replace",
        index=False
    )

    bank_responses.to_sql(
        "bank_response_codes",
        engine,
        if_exists="replace",
        index=False
    )

    print("\nAll cleaned tables successfully saved to SQLite.")

def load_from_database():
    """
    Load cleaned transaction data from SQLite database.
    """

    query = """
    SELECT
        t."Transaction ID",
        t."Timestamp",
        t."Sender Name",
        t."Sender UPI ID",
        t."Receiver Name",
        t."Receiver UPI ID",
        t."Amount (INR)",
        t."Status",
        t."Is_Outlier",
        t."Valid_Amount",
        t."Valid_Status",
        t."Valid_Sender_UPI",
        t."Valid_Receiver_UPI",
        t."Passes_All_Checks",
        p."Retry Count",
        b."Response Code",
        b."Response Description"
    FROM transactions_cleaned t
    LEFT JOIN payment_retries p
        ON t."Transaction ID" = p."Transaction ID"
    LEFT JOIN bank_response_codes b
        ON t."Transaction ID" = b."Transaction ID"
    """

    df = pd.read_sql(query, engine)

    return df


def check_database_schema():
    """
    Display the schema of the transactions_cleaned table.
    """

    inspector = inspect(engine)

    columns = inspector.get_columns("transactions_cleaned")

    print("\n" + "=" * 50)
    print("DATABASE SCHEMA")
    print("=" * 50)

    for column in columns:
        print(f"{column['name']} : {column['type']}")