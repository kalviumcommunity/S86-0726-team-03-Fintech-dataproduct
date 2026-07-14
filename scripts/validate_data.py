def validate_data(df):
    """
    Validate important columns in the dataset.
    """

    print("=" * 50)
    print("DATA VALIDATION")
    print("=" * 50)

    # Amount should be greater than 0
    df["Valid_Amount"] = df["Amount (INR)"] > 0

    # Status should contain only valid values
    valid_status = ["SUCCESS", "FAILED", "PENDING"]
    df["Valid_Status"] = df["Status"].isin(valid_status)

    # Sender and Receiver UPI IDs should contain '@'
    df["Valid_Sender_UPI"] = df["Sender UPI ID"].str.contains("@", na=False)
    df["Valid_Receiver_UPI"] = df["Receiver UPI ID"].str.contains("@", na=False)

    # Overall validation
    validation_columns = [
        "Valid_Amount",
        "Valid_Status",
        "Valid_Sender_UPI",
        "Valid_Receiver_UPI"
    ]

    df["Passes_All_Checks"] = df[validation_columns].all(axis=1)

    print(f"Total Records : {len(df)}")
    print(f"Passed : {df['Passes_All_Checks'].sum()}")
    print(f"Failed : {(~df['Passes_All_Checks']).sum()}")

    return df