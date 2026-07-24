CREATE VIEW vw_failure_amount_distribution AS

WITH categorized_failures AS (
    SELECT
        CASE
            WHEN "Amount (INR)" <= 500
                THEN '₹0–₹500'
            WHEN "Amount (INR)" <= 1000
                THEN '₹500–₹1,000'
            WHEN "Amount (INR)" <= 2500
                THEN '₹1,000–₹2,500'
            WHEN "Amount (INR)" <= 5000
                THEN '₹2,500–₹5,000'
            WHEN "Amount (INR)" <= 7500
                THEN '₹5,000–₹7,500'
            WHEN "Amount (INR)" <= 10000
                THEN '₹7,500–₹10,000'
        END AS amount_range

    FROM transactions

    WHERE "Status" = 'FAILED'
)

SELECT
    amount_range,
    COUNT(*) AS failed_transaction_count

FROM categorized_failures

GROUP BY amount_range;