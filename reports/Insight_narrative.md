# Data Storytelling & Insight Narrative – Fintech Payment Analytics

## 1. Context

The fintech payment analytics project was developed to understand payment success and failure patterns and identify opportunities to improve payment recovery. Payment failures can result in lost revenue and customer frustration, especially when customers repeatedly attempt transactions without successfully completing them.

The analysis focuses on understanding transaction outcomes, failure reasons, retry behaviour, and bank response patterns so that temporary payment friction can be distinguished from potentially recoverable revenue loss.

---

## 2. Data

The analysis was performed on a dataset containing **1,000 UPI payment transactions**. The dataset includes transaction details such as transaction ID, timestamp, sender and receiver information, transaction amount, and payment status.

Additional datasets containing **payment retry information** and **bank response codes** were joined using the **Transaction ID** to provide a broader view of transaction behaviour.

The data was cleaned, validated, and stored in a SQL database. The analysis used the cleaned and joined data to examine transaction success and failure rates, failure reasons, retry patterns, and transaction behaviour across different hours of the day.

---

## 3. Findings

### Finding 1: Payment Success and Failure Rates Are Almost Evenly Split

Out of **1,000 total transactions**, **502 transactions were successful**, while **498 transactions failed**.

This results in a **50.2% success rate** and a **49.8% failure rate**.

The near-even split between successful and failed transactions indicates that payment failures represent a significant part of the overall transaction activity rather than being an isolated issue.

**Business Implication:**
A large proportion of transactions are currently failing, which means there may be a significant opportunity to improve payment reliability and recover transactions that could otherwise result in lost revenue.

---

### Finding 2: Failed Transactions Represent a Significant Revenue Opportunity

The dataset contains approximately **₹49.99 lakh** in total transaction value.

Successful transactions account for approximately **₹25.40 lakh**, while failed transactions represent approximately **₹24.59 lakh** in transaction value.

Almost half of the analyzed payment attempts failed, representing ₹24.59 lakh in transaction value that could potentially be recovered through smarter failure classification and targeted retry strategies.

**Business Implication:**
Not every failed transaction represents permanently lost revenue, but the high value associated with failures suggests that identifying recoverable failures should be a major priority.
The failed transaction value should therefore be considered a **potential recovery opportunity**, rather than automatically being treated as permanently lost revenue.

---

### Finding 3: Insufficient Funds and Do Not Honor Are Major Failure Reasons

The failure-reason analysis shows that **Insufficient Funds** and **Do Not Honor** are among the most frequent failure reasons.

Other observed failure reasons include:

- Customer Unavailable
- Invalid Transaction
- Expired Card

The distribution shows that failures are not caused by a single issue. Some failures may be recoverable through retry strategies, while others may require customer action or cannot be recovered immediately.

**Business Implication:**

Failure reasons should be categorized into **recoverable** and **non-recoverable** groups. This would allow the system to determine which failed transactions should be retried automatically and which should instead be communicated to the customer for corrective action.

For example, failures caused by insufficient funds may require the customer to add funds before attempting the payment again, while certain bank authorization failures may require a different recovery approach.

---

### Finding 4: Most Transactions Do Not Require Retries

The retry distribution shows that the majority of transactions have a **retry count of 0**.

A smaller number of transactions have **1 or more retries**, with very few transactions reaching **3 retries**.

This indicates that most transactions either succeed or fail without repeated attempts, while a smaller group of transactions experiences repeated payment friction.

**Business Implication:**

The retry dataset can be used to identify transactions where additional recovery attempts may be useful. However, retries should be controlled based on the failure reason and bank response rather than blindly retrying every failed payment.

A targeted retry strategy could help avoid unnecessary repeated attempts while focusing recovery efforts on transactions with a higher likelihood of successful completion.

---

### Finding 5: Payment Failures Occur Throughout the Day

The hourly failure analysis shows that failed transactions occur across different hours rather than being restricted to a single period.

Some hours show higher failure counts than others, with the highest observed failure activity occurring around **16:00**.

However, the variation across hours does not by itself prove that time of day is the root cause of failures.

**Business Implication:**

Hourly analysis can help identify potential periods of increased payment friction and can be combined with bank response codes, failure reasons, and retry behaviour to determine whether specific time periods require further investigation.

Further analysis would be required before concluding that a particular time period directly causes higher payment failure rates.

---

## 4. Why Are These Patterns Occurring?

The analysis suggests that payment failures are caused by a combination of different factors rather than one single problem.

Some failures, such as **Insufficient Funds**, may require the customer to add funds before attempting the transaction again. Other responses, such as **Do Not Honor**, may be related to bank authorization decisions and may require different recovery strategies.

The presence of different failure reasons indicates that not all failed payments should be handled in the same way. A failure caused by insufficient funds may require customer action, while a temporary or potentially recoverable failure may be suitable for a controlled retry.

The retry analysis also shows that repeated attempts are relatively limited across the dataset. This creates an opportunity to introduce a more intelligent recovery strategy in which the system considers the failure reason and bank response before deciding whether a transaction should be retried.

For example, potentially temporary failures could be prioritized for controlled retries, while failures requiring customer intervention should be communicated clearly instead of repeatedly retrying the payment.

The analysis therefore suggests that a **failure-reason-based recovery strategy** could be more effective than applying a single retry rule to all failed transactions.

---

## 5. Recommended Actions

### Recommendation 1: Create Failure-Recovery Categories

Classify payment failures into categories such as:

- **Retryable** – potentially temporary failures that may succeed if attempted again
- **Customer Action Required** – failures such as insufficient funds that require the customer to take action
- **Bank Authorization Failure** – bank-related declines that may require a different payment method or bank-level investigation
- **Non-Recoverable** – failures unlikely to succeed through automatic retries

**Owner:** Payment Engineering / Data Team

**Timeline:** Implement during the next recovery pipeline development cycle.

**Expected Impact:** Better targeting of recovery attempts and reduced unnecessary retries.

---

### Recommendation 2: Introduce Intelligent Retry Rules

Instead of retrying every failed transaction, use the **failure reason**, **response code**, and **retry count** to determine whether another attempt should be made.

For example, if a transaction has a retryable failure and has not exceeded the retry threshold, it can be considered for another attempt.

If the transaction has already reached the retry limit, it should be stopped and classified as unrecovered.

This approach would allow the payment recovery process to prioritize transactions that have a higher probability of successful recovery.

**Owner:** Payment Engineering Team

**Timeline:** After failure categories are finalized.

**Expected Impact:** Improved recovery efficiency while avoiding excessive or unnecessary retries.

---

### Recommendation 3: Monitor High-Value Failed Transactions

Since failed transactions represent approximately **₹24.59 lakh in transaction value** in the analyzed dataset, high-value failed payments should be monitored separately.

The business could prioritize recovery efforts based on:

- Transaction amount
- Failure reason
- Retry count
- Bank response code

This would help the business focus recovery efforts on failed transactions that have a greater potential revenue impact.

**Owner:** Finance and Payment Operations

**Timeline:** Include in the next dashboard iteration.

**Expected Impact:** Focus recovery efforts on transactions with the highest potential revenue impact.

---

### Recommendation 4: Monitor Bank Response Patterns

Bank response codes should be analyzed alongside failure descriptions to identify whether particular banks or response codes contribute disproportionately to payment failures.

This analysis can help distinguish between:

- Customer-related failures
- Bank-side failures
- Temporary technical issues
- Authorization-related declines

Monitoring these patterns over time can help identify recurring payment issues and determine whether certain bank responses require additional investigation.

**Owner:** Payment Operations / Data Analytics Team

**Timeline:** Ongoing monitoring through the analytics dashboard.

**Expected Impact:** Faster identification of recurring bank-level payment issues and improved understanding of payment failure patterns.

---

## Conclusion

The analysis of **1,000 UPI transactions** shows that payment failures represent a significant part of the overall payment activity, with **498 failed transactions compared with 502 successful transactions**. This results in a **50.2% transaction success rate**.

Failed transactions represent approximately **₹24.59 lakh in transaction value**, highlighting a potentially significant recovery opportunity. However, this value should not automatically be considered permanently lost revenue because some customers may retry successfully or complete their payment through another method.

The analysis also shows that payment failures are caused by multiple factors, including **Insufficient Funds** and **Do Not Honor**, while most transactions do not involve repeated retries.

These findings suggest that payment recovery should not rely on a single retry strategy. Instead, recovery decisions should consider the **failure reason, bank response code, transaction value, and retry history**.

The recommended next step is to develop a more intelligent payment recovery strategy that identifies which failed transactions are suitable for retry, which require customer action, and which should be classified as unrecovered. This can help the business focus recovery efforts on transactions with the highest likelihood of successful recovery and the greatest potential revenue impact.