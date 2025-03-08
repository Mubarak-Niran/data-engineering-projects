-- Find duplicate rows
SELECT *, COUNT(*)
FROM `project.dataset.table`
GROUP BY 1, 2, 3 -- Adjust columns
HAVING COUNT(*) > 1;

-- Example window function
SELECT *,
    ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY transaction_date DESC) AS rn
FROM `project.dataset.transactions`;

-- Partitioned table scan example
SELECT *
FROM `project.dataset.partitioned_table`
WHERE date_column = DATE('2025-03-07');
