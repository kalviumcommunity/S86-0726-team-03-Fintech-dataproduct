CREATE VIEW IF NOT EXISTS vw_revenue_by_status AS
SELECT
    Status,
    SUM("Amount (INR)") AS total_revenue
FROM transactions_cleaned
GROUP BY Status
ORDER BY total_revenue DESC;