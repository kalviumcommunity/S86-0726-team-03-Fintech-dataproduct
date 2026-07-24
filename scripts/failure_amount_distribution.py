import matplotlib.pyplot as plt
import pandas as pd


def failure_amount_distribution(df):

    print("=" * 60)
    print("FAILED PAYMENT AMOUNT DISTRIBUTION")
    print("=" * 60)

    # -------------------------------
    # Filter Failed Transactions
    # -------------------------------

    failed_df = df[df["Status"] == "FAILED"].copy()

    # -------------------------------
    # Create Amount Ranges
    # -------------------------------

    bins = [
        0,
        500,
        1000,
        2500,
        5000,
        7500,
        10000
    ]

    labels = [
        "₹0–₹500",
        "₹500–₹1,000",
        "₹1,000–₹2,500",
        "₹2,500–₹5,000",
        "₹5,000–₹7,500",
        "₹7,500–₹10,000"
    ]

    failed_df["Amount Range"] = pd.cut(
        failed_df["Amount (INR)"],
        bins=bins,
        labels=labels,
        include_lowest=True
    )

    amount_distribution = (
        failed_df["Amount Range"]
        .value_counts()
        .sort_index()
    )

    print("\nFailed Transaction Amount Distribution\n")
    print(amount_distribution)

    # -------------------------------
    # Visualization
    # -------------------------------

    plt.figure(figsize=(10, 6))

    amount_distribution.plot(kind="bar")

    plt.title("Failed Transaction Amount Distribution")
    plt.xlabel("Transaction Amount Range")
    plt.ylabel("Number of Failed Transactions")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()