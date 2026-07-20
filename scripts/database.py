import pandas as pd
from sqlalchemy import create_engine, inspect


# Create SQLite database connection
DATABASE_URL = "sqlite:///analytics.db"

engine = create_engine(DATABASE_URL)


def save_to_database(df):
    """
    Save cleaned DataFrame to SQLite database.
    """

    df.to_sql(
        "transactions_cleaned",
        engine,
        if_exists="replace",
        index=False
    )

    print("\nCleaned data successfully saved to SQLite database.")


def load_from_database():
    """
    Load cleaned transaction data from SQLite database.
    """

    query = """
    SELECT *
    FROM transactions_cleaned
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