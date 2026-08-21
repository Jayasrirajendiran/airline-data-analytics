-- =========================================================
-- AIRLINE DATA ANALYTICS
-- COMPREHENSIVE BUSINESS ANALYSIS QUERIES (PostgreSQL)
-- =========================================================

-- 1. OVERALL AIRLINE EXECUTIVE KPIS
SELECT
    COUNT(*) AS total_flights,
    SUM(passengers) AS total_passengers,
    ROUND(SUM(total_revenue), 2) AS total_revenue,
    ROUND(SUM(total_cost), 2) AS total_cost,
    ROUND(SUM(profit), 2) AS total_profit,
    ROUND(SUM(profit) / NULLIF(SUM(total_revenue), 0) * 100, 2) AS profit_margin_pct
FROM airline_data;

-- 2. MONTHLY PERFORMANCE TREND
SELECT
    year,
    month_number,
    month,
    COUNT(*) AS total_flights,
    SUM(passengers) AS total_passengers,
    ROUND(SUM(total_revenue), 2) AS total_revenue,
    ROUND(SUM(profit), 2) AS total_profit
FROM airline_data
GROUP BY year, month_number, month
ORDER BY year, month_number;

-- 3. MONTH-OVER-MONTH REVENUE GROWTH
WITH monthly_revenue AS (
    SELECT year, month_number, month, SUM(total_revenue) AS revenue
    FROM airline_data
    GROUP BY year, month_number, month
),
revenue_lag AS (
    SELECT year, month_number, month, revenue,
           LAG(revenue) OVER (ORDER BY year, month_number) AS previous_month_revenue
    FROM monthly_revenue
)
SELECT year, month_number, month,
       ROUND(revenue, 2) AS total_revenue,
       ROUND(previous_month_revenue, 2) AS previous_month_revenue,
       ROUND((revenue - previous_month_revenue) / NULLIF(previous_month_revenue, 0) * 100, 2) AS mom_growth_pct
FROM revenue_lag
ORDER BY year, month_number;

-- 4. TOP 10 PROFITABLE ROUTES
SELECT route, COUNT(*) AS total_flights, ROUND(SUM(total_revenue), 2) AS total_revenue, ROUND(SUM(profit), 2) AS total_profit
FROM airline_data
GROUP BY route
ORDER BY total_profit DESC
LIMIT 10;

-- 5. PERSISTENTLY LOSS-MAKING ROUTES AUDIT
SELECT route, COUNT(*) AS total_flights, ROUND(SUM(total_revenue), 2) AS total_revenue, ROUND(SUM(profit), 2) AS total_loss
FROM airline_data
GROUP BY route
HAVING SUM(profit) < 0
ORDER BY total_loss ASC;
