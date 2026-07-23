SELECT
    t.*,
    p."Retry Count",
    b."Response Code",
    b."Response Description"
FROM transactions_cleaned t
LEFT JOIN payment_retries p
    ON t."Transaction ID" = p."Transaction ID"
LEFT JOIN bank_response_codes b
    ON t."Transaction ID" = b."Transaction ID";