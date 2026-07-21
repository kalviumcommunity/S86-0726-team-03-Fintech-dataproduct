SELECT
    "Sender UPI ID",
    COUNT(*) AS transaction_count,
    SUM("Amount (INR)") AS total_amount
FROM transactions_cleaned
WHERE Status = 'SUCCESS'
GROUP BY "Sender UPI ID"
ORDER BY total_amount DESC
LIMIT 10;