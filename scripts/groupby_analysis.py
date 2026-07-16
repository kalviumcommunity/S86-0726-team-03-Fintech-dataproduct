def groupby_analysis(df):

    print("=" * 50)
    print("GROUPBY ANALYSIS")
    print("=" * 50)

    # Total Transaction Amount by Status
    print("\nTotal Amount by Status:")
    print(df.groupby("Status")["Amount (INR)"].sum())

    # Number of Transactions by Status
    print("\nTransaction Count by Status:")
    print(df.groupby("Status")["Transaction ID"].count())

    # Average Transaction Amount by Status
    print("\nAverage Amount by Status:")
    print(df.groupby("Status")["Amount (INR)"].mean())