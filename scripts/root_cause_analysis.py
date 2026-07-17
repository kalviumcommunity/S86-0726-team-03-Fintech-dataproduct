import matplotlib.pyplot as plt


def root_cause_analysis(df):

    print("=" * 60)
    print("ROOT CAUSE INVESTIGATION")
    print("=" * 60)

    # -------------------------------
    # Overall Statistics
    # -------------------------------

    total_transactions = len(df)

    successful = len(df[df["Status"] == "SUCCESS"])
    failed = len(df[df["Status"] == "FAILED"])

    success_rate = (successful / total_transactions) * 100
    failure_rate = (failed / total_transactions) * 100

    print(f"\nTotal Transactions : {total_transactions}")
    print(f"Successful         : {successful}")
    print(f"Failed             : {failed}")
    print(f"Success Rate       : {success_rate:.2f}%")
    print(f"Failure Rate       : {failure_rate:.2f}%")

    # -------------------------------
    # Failure Reasons
    # -------------------------------

    failure_reasons = (
        df[df["Status"] == "FAILED"]
        .groupby("Response Description")
        .size()
        .sort_values(ascending=False)
    )

    print("\nTop Failure Reasons\n")
    print(failure_reasons)

    # -------------------------------
    # Failure by Hour
    # -------------------------------

    failed_df = df[df["Status"] == "FAILED"].copy()

    failed_df["Hour"] = failed_df["Timestamp"].dt.hour

    hourly_failures = failed_df.groupby("Hour").size()

    print("\nFailures by Hour\n")
    print(hourly_failures)

    # -------------------------------
    # Retry Analysis
    # -------------------------------

    retry_summary = (
        df["Retry Count"]
        .value_counts()
        .sort_index()
    )

    print("\nRetry Analysis\n")
    print(retry_summary)

    print(f"\nAverage Retry Count : {df['Retry Count'].mean():.2f}")
    print(f"Maximum Retry Count : {df['Retry Count'].max()}")

    # ==================================================
    #                VISUALIZATIONS
    # ==================================================

    plt.figure(figsize=(16,10))

    # ---------------------------------
    # Chart 1 : Success vs Failed
    # ---------------------------------

    plt.subplot(2,2,1)

    plt.bar(
        ["Success", "Failed"],
        [successful, failed]
    )

    plt.title("Success vs Failed Transactions")
    plt.ylabel("Number of Transactions")


    # ---------------------------------
    # Chart 2 : Failure Reasons
    # ---------------------------------

    plt.subplot(2,2,2)

    failure_reasons.plot(kind="bar")

    plt.title("Top Failure Reasons")
    plt.xlabel("Response Description")
    plt.ylabel("Failed Transactions")


    # ---------------------------------
    # Chart 3 : Failure by Hour
    # ---------------------------------

    plt.subplot(2,2,3)

    hourly_failures.plot(kind="bar")

    plt.title("Failed Transactions by Hour")
    plt.xlabel("Hour")
    plt.ylabel("Failed Transactions")


    # ---------------------------------
    # Chart 4 : Retry Count Distribution
    # ---------------------------------

    plt.subplot(2,2,4)

    retry_summary.plot(kind="bar")

    plt.title("Retry Count Distribution")
    plt.xlabel("Retry Count")
    plt.ylabel("Number of Transactions")


    plt.tight_layout()

    plt.show()