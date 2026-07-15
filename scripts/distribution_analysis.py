import matplotlib.pyplot as plt
def distribution_analysis(df):
    """
    Analyze the distribution of transaction amounts.
    """

    print("=" * 50)
    print("DISTRIBUTION ANALYSIS")
    print("=" * 50)

    # Basic statistics
    print("\nTransaction Amount Statistics:")
    print(df["Amount (INR)"].describe())

    # Skewness
    skew = df["Amount (INR)"].skew()
    print(f"\nSkewness: {skew:.2f}")

    if skew > 1:
        print("Data is positively skewed.")
    elif skew < -1:
        print("Data is negatively skewed.")
    else:
        print("Data is approximately symmetric.")

    # Histogram
    plt.figure(figsize=(8,5))
    plt.hist(df["Amount (INR)"], bins=20, edgecolor="black")
    plt.title("Transaction Amount Distribution")
    plt.xlabel("Amount (INR)")
    plt.ylabel("Number of Transactions")
    plt.show()