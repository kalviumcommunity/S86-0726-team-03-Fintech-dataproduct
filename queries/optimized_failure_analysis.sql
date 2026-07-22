WITH failed_transactions AS (
    SELECT
        "Transaction ID",
        "Amount (INR)",
        "Response Description"
    FROM transactions_cleaned
    WHERE "Status" = 'FAILED'
)
SELECT
    "Response Description",
    COUNT(*) AS failure_count,
    SUM("Amount (INR)") AS total_failed_amount
FROM failed_transactions
GROUP BY "Response Description"
ORDER BY failure_count DESC;