SELECT
    Status,
    COUNT(*) AS transaction_count,
    SUM("Amount (INR)") AS total_amount,
    AVG("Amount (INR)") AS average_amount
FROM transactions_cleaned
GROUP BY Status
ORDER BY transaction_count DESC;