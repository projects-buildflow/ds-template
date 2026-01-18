-- SLOW QUERY: Daily Revenue Report
-- This query is taking 30+ seconds to run and blocking other reports.
-- Your task: Optimize it without changing the results.

-- The query calculates daily revenue with customer segment breakdown.
-- Current issues: nested subqueries, SELECT *, redundant calculations, no index usage

SELECT *
FROM (
    SELECT
        DATE(o.order_date) as report_date,
        (
            SELECT COUNT(*)
            FROM orders o2
            WHERE DATE(o2.order_date) = DATE(o.order_date)
        ) as total_orders,
        (
            SELECT SUM(o3.total)
            FROM orders o3
            WHERE DATE(o3.order_date) = DATE(o.order_date)
        ) as daily_revenue,
        (
            SELECT AVG(o4.total)
            FROM orders o4
            WHERE DATE(o4.order_date) = DATE(o.order_date)
        ) as avg_order_value,
        (
            SELECT COUNT(DISTINCT o5.customer_id)
            FROM orders o5
            WHERE DATE(o5.order_date) = DATE(o.order_date)
        ) as unique_customers,
        (
            SELECT
                CASE
                    WHEN c.total_orders > 10 THEN 'high_value'
                    WHEN c.total_orders > 3 THEN 'medium_value'
                    ELSE 'low_value'
                END
            FROM customers c
            WHERE c.customer_id = o.customer_id
        ) as customer_segment,
        (
            SELECT SUM(total)
            FROM orders
            WHERE customer_id = o.customer_id
            AND DATE(order_date) <= DATE(o.order_date)
        ) as customer_lifetime_value_to_date,
        (
            SELECT
                ROUND(
                    (
                        SELECT SUM(total) FROM orders
                        WHERE DATE(order_date) = DATE(o.order_date)
                    ) /
                    NULLIF(
                        (
                            SELECT SUM(total) FROM orders
                            WHERE DATE(order_date) = DATE(o.order_date) - INTERVAL '1 day'
                        ),
                        0
                    ) * 100 - 100,
                    2
                )
        ) as day_over_day_growth_pct
    FROM orders o
    WHERE o.order_date >= '2024-01-01'
    ORDER BY o.order_date, o.order_id
) AS daily_report
WHERE report_date IS NOT NULL
ORDER BY report_date DESC;

-- Problems with this query:
-- 1. SELECT * at outer query pulls all columns unnecessarily
-- 2. Multiple correlated subqueries recalculate the same aggregations
-- 3. DATE() function on order_date prevents index usage
-- 4. Customer segment is calculated per-row instead of joined once
-- 5. Customer lifetime value recalculates entire history for each order
-- 6. Day-over-day calculation has deeply nested subqueries
-- 7. No use of window functions where appropriate
-- 8. Redundant ORDER BY in inner query
-- 9. Could benefit from CTEs for readability and potential optimization

-- Expected output columns:
-- report_date, total_orders, daily_revenue, avg_order_value,
-- unique_customers, customer_segment, customer_lifetime_value_to_date,
-- day_over_day_growth_pct
