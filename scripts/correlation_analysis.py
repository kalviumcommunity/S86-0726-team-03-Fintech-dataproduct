import matplotlib.pyplot as plt

def correlation_analysis(df):

    print("=" * 50)
    print("CORRELATION ANALYSIS")
    print("=" * 50)

    numeric_df = df[
    [
        "Amount (INR)",
        "Retry Count",
        "Response Code"
    ]
]
    # Calculate correlation matrix
    corr_matrix = numeric_df.corr()

    print("\nCorrelation Matrix:\n")
    print(corr_matrix)

    # Plot heatmap
    plt.figure(figsize=(8,6))
    plt.imshow(corr_matrix, cmap="coolwarm", interpolation="nearest")
    plt.colorbar()

    plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns, rotation=45)
    plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)

    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()