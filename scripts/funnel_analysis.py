import matplotlib.pyplot as plt

def funnel_analysis(df):

    print("=" * 50)
    print("FUNNEL ANALYSIS")
    print("=" * 50)

    total_transactions = len(df)

    retry_transactions = (df["Retry Count"] > 0).sum()

    successful_transactions = (df["Status"] == "SUCCESS").sum()

    stages = {
        "Total": total_transactions,
        "Retried": retry_transactions,
        "Successful": successful_transactions
    }

    print("\nFunnel Stages:")
    print(stages)

    plt.figure(figsize=(6,4))
    plt.bar(stages.keys(), stages.values())
    plt.title("Payment Funnel")
    plt.ylabel("Transactions")
    plt.show()