SELECT TOP 10 * FROM dbo.fact_transactions;


SELECT TOP 10 * FROM dbo.dim_devices

SELECT TOP 10 * from dim_users


SELECT TOP 10 * FROM dbo.dim_medications


---------------- Total Transactions by Type-------------------
--------------------------------------------------------------   
-- 1) Remove has the most transactions followed by Waste and Refill

SELECT transaction_type, COUNT(*) as total_transactions FROM dbo.fact_transactions
GROUP BY transaction_type 
ORDER BY total_transactions DESC;

------------------ Top 10 most dispensed medications-----------
---------------------------------------------------------------
-- 1) med Piperacillin-Tazobactam 3.375G is highest dispensed med in the organization at 45 dispenses
-- 2) Followed by Vancomycin 1G at 39 and Lactated Ringers 1L at 37

SELECT meds.medication_name, tx.transaction_type, COUNT(tx.transaction_id) as Total_dispensed 
FROM fact_transactions tx
JOIN dim_medications meds
ON tx.medication_id = meds.medication_id
WHERE tx.transaction_type = 'Remove'
GROUP BY meds.medication_name, tx.transaction_type
ORDER BY Total_dispensed DESC

-- Transaction Volume by Department

SELECT d.department, COUNT(*) as total
FROM fact_transactions tx
JOIN dim_devices d
on tx.device_id = d.device_id
GROUP BY d.department
ORDER BY total DESC;


-- Total discrepancies by Medication Class

SELECT meds.medication_name, 
		meds.medication_class, 
		CASE 
			WHEN meds.medication_class IN (0,1,2) then 'Controlled' 
			ELSE 'Non-controlled'
		END as controlled_label,
		SUM(tx.discrepancy_flag) as total_discrepancies
FROM fact_transactions tx
JOIN dim_medications meds
ON tx.medication_id = meds.medication_id
WHERE tx.discrepancy_flag = 1
GROUP BY meds.medication_name, meds.medication_class
ORDER BY total_discrepancies DESC;

-- Users with most overrides (top 10)

SELECT TOP 10 (u.user_id),u.user_name, u.user_role, tx.transaction_type
FROM fact_transactions tx
JOIN dim_users u
ON tx.user_id = u.user_id
WHERE transaction_type = 'Override'

-- Override rate per user (Overide / total_transactions)

WITH override_stats AS (
	SELECT u.user_name,
			u.user_id,
			u.user_role,
			COUNt(*) as total_tx,
			SUM(CASE WHEN tx.transaction_type = 'Override' THEN 1 ELSE 0 END) as override_tx
	FROM fact_transactions tx
	JOIN dim_users u ON tx.user_id = u.user_id
	GROUP BY u.user_name, u.user_role, u.user_id
	HAVINg Count(*) > 10
)

SELECT	TOP 10
		user_name,
		user_role,
		CONCAT(ROUND(override_tx * 100.0/ total_tx, 1), '%') as override_percentage
FROM override_stats
ORDER BY override_percentage DESC

-- Controlled med Return/Waste transactions missing witness (compliance breach)

-- ══════════════════════════════════════════════
-- Controlled med Return/Waste missing witness
-- ══════════════════════════════════════════════
-- Finding: 0 results — 100% witness compliance
-- All controlled medication Return/Waste
-- All transactions had a witness present

SELECT tx.transaction_id, 
		tx.transaction_type,
		meds.medication_name,
		meds.medication_class,
		tx.witness_name
FROM fact_transactions tx 
JOIN dim_medications meds On tx.medication_id = meds.medication_id
WHERE tx.transaction_type IN ('Return','Waste') 
AND meds.is_controlled = 1
AND tx.witness_name IS NULL
ORDER BY meds.medication_class



-- Discrepancy rate for controlled vs non-controlled medications

SELECT	meds.medication_name,
		CASE WHEN meds.is_controlled = 1 
			THEN 'Controlled' 
			ELSE 'Non-Controlled' END as Medication_type,
		COUNT(*) as total_transactions,
		SUM(tx.discrepancy_flag) as total_discrepancies,
		ROUND(SUM(tx.discrepancy_flag) * 100.0/ COUNT(*), 1) as discrepancy_rate
		FROM fact_transactions tx
JOIN dim_medications meds ON tx.medication_id = meds.medication_id
GROUP BY meds.is_controlled, meds.medication_name
ORDER BY discrepancy_rate DESC

-- Rank users by override count within each department

WITH override_counts as (
	SELECT	u.user_name,
			d.department,
			COUNT(*) as override_count
	FROM fact_transactions tx
	JOIN dim_users u ON tx.user_id = u.user_id
	JOIN dim_devices d ON tx.device_id = d.device_id
	WHERE tx.transaction_type = 'Override'
	GROUP BY d.department, u.user_name
)

SELECT *, DENSE_RANK() OVER(PARTITION BY department ORDER BY override_count DESC) as rank
FROM override_counts

-- Running total of transaactions by Month


WITH monthly_tx as (
	SELECT MONTH(transaction_datetime) as months,
	COUNT(*) as tx_count
	FROM fact_transactions
	GROUP BY MONTH(transaction_datetime)
)
SELECT months, tx_count, SUM(tx_count) OVER(ORDER BY months) as running_total
from monthly_tx



-- Find devices with above average discrepancy rates

WITH avg_rate AS (
    SELECT
        d.device_name,
        COUNT(*) as total_tx,
        AVG(CAST(tx.discrepancy_flag AS FLOAT)) as disc_rate
    FROM fact_transactions tx
    JOIN dim_devices d ON tx.device_id = d.device_id
    GROUP BY d.device_name
)
SELECT
    device_name,
    total_tx,
    CONCAT(ROUND(disc_rate * 100, 2), '%' ) as disc_rate_pct
FROM avg_rate
WHERE disc_rate > (SELECT AVG(disc_rate) FROM avg_rate)
ORDER BY disc_rate_pct DESC









		