CREATE VIEW IF NOT EXISTS vw_failure_analysis AS
SELECT
    "Response Description",
    COUNT(*) AS failure_count
FROM transactions_cleaned
WHERE Status = 'FAILED'
GROUP BY "Response Description"
ORDER BY failure_count DESC;