import pandas as pd

def ingest_csv(filepath):
    df = pd.read_csv(
        filepath,
        delimiter=",",
        encoding="utf-8"
    )

    print("CSV Loaded Successfully")
    print(df.shape)
    print(df.head())

    return df


if __name__ == "__main__":
    csv_df = ingest_csv("data/raw/transactions.csv")