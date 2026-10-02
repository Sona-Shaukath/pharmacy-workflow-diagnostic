-- Pharmacy Workflow & Inventory Diagnostic Queries

-- 1. Identify Bottleneck Processing Stages (P90 Duration & Failures)
SELECT 
    stage,
    COUNT(rx_id) AS total_processed,
    ROUND(AVG(duration_seconds), 2) AS avg_duration_sec,
    PERCENTILE_CONT(0.90) WITHIN GROUP (ORDER BY duration_seconds) AS p90_duration_sec,
    SUM(CASE WHEN status IN ('REJECTED_INSURANCE', 'TIMEOUT') THEN 1 ELSE 0 END) AS adjudication_failures
FROM raw_prescription_logs
GROUP BY stage
ORDER BY avg_duration_sec DESC;

-- 2. Low-Stock Automated Re-order Alert Query
SELECT 
    med_id,
    med_name,
    category,
    current_stock,
    reorder_threshold,
    reorder_qty,
    CASE 
        WHEN current_stock <= reorder_threshold THEN 'CRITICAL: REORDER REQUIRED'
        ELSE 'STABLE'
    END AS stock_status
FROM inventory_data
WHERE current_stock <= reorder_threshold
ORDER BY current_stock ASC;
