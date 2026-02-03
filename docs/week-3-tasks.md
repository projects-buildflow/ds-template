# Week 3: Business Analysis

"Revenue dropped. The CEO wants answers."

Welcome to Week 3! You've proven you can handle data quality. Now it's time to solve real business problems.

---

## Task 3.1: Revenue Investigation (100 XP)

**Objective:** Investigate the revenue drop and present your findings.

### The Situation:
Meera (CEO) just sent an urgent Slack message: "Revenue is down 15% this month. I need to understand why before the board meeting next week."

Priya has assigned this to you. Time to put your analysis skills to work.

### Steps:
1. Create a Jupyter notebook: `revenue_investigation.ipynb`
2. Analyze the data in `data/orders.csv` and `data/customers.csv`
3. Your notebook must include these sections:
   - **Executive Summary**: Key finding in 2-3 sentences
   - **Analysis**: Charts and tables supporting your findings
   - **Root Cause**: What's causing the revenue drop?
   - **Recommendations**: 2-3 actionable suggestions

### Hints:
- Look at order volume vs. average order value
- Check for changes in customer segments
- Consider seasonal patterns
- Don't just describe what happened - explain *why*

### Example structure:
```python
# Executive Summary
"""
Revenue declined 15% primarily due to [finding].
This is driven by [root cause].
Recommend [action] to address this.
"""

# Analysis
import pandas as pd
import matplotlib.pyplot as plt

orders = pd.read_csv('data/orders.csv')
# Your analysis here...
```

### Test locally:
```bash
pytest tests/test_3_1.py -v
```

### Evaluation:
AI-powered notebook review for completeness and insight quality.

---

## Task 3.2: SQL Cohort Analysis (75 XP)

**Objective:** Build a customer retention cohort analysis using SQL.

### The Situation:
Vikram (Product Manager) wants to understand customer retention patterns. He needs a cohort analysis showing how many customers return each month after their first purchase.

### Steps:
1. Create: `cohort_analysis.sql`
2. Write a query that:
   - Groups customers by their first purchase month (cohort)
   - Shows retention for months 0, 1, 2, 3, 4, 5
   - Uses the orders data (assume SQLite or PostgreSQL syntax)

### Expected output format:
| cohort_month | month_0 | month_1 | month_2 | month_3 | month_4 | month_5 |
|--------------|---------|---------|---------|---------|---------|---------|
| 2024-01      | 100     | 45      | 32      | 28      | 25      | 22      |
| 2024-02      | 120     | 52      | 38      | 30      | 27      | NULL    |
| ...          | ...     | ...     | ...     | ...     | ...     | ...     |

### Example approach:
```sql
WITH customer_cohorts AS (
    SELECT
        customer_id,
        DATE_TRUNC('month', MIN(order_date)) AS cohort_month
    FROM orders
    GROUP BY customer_id
),
cohort_orders AS (
    -- Join back to get all orders with cohort info
    -- Calculate months since first purchase
)
SELECT
    cohort_month,
    COUNT(DISTINCT CASE WHEN months_since_first = 0 THEN customer_id END) AS month_0,
    -- ... continue for other months
FROM cohort_orders
GROUP BY cohort_month
ORDER BY cohort_month;
```

### Test locally:
```bash
pytest tests/test_3_2.py -v
```

### Evaluation:
PR-based with query execution and output validation.

---

## Task 3.3: Query Optimization (75 XP)

**Objective:** Optimize a slow SQL query.

### The Situation:
Ananya found a query that's taking 30+ seconds to run. It's blocking other reports. Your job: make it faster without changing the results.

### Steps:
1. Look at `week-3/task-3.3/slow_query.sql` (the original slow query)
2. Create: `optimized_query.sql`
3. Create: `optimization_notes.md` explaining:
   - What made the original query slow
   - What changes you made
   - Why your changes improve performance

### Optimization techniques to consider:
- Remove unnecessary columns (SELECT * is often bad)
- Avoid nested subqueries when joins would work
- Use appropriate indexes (document which ones would help)
- Eliminate redundant calculations
- Consider query execution order

### Test locally:
```bash
pytest tests/test_3_3.py -v
```

### Evaluation:
PR-based with output comparison and documentation review.

---

## Task 3.4: Dashboard Creation (100 XP)

**Objective:** Create a business dashboard for the executive team.

### The Situation:
Meera loved your revenue analysis! Now she wants a dashboard the team can check weekly. Create a simple dashboard showing key business metrics.

### Steps:
1. Create a dashboard using any tool (Streamlit, Dash, Metabase, or even Google Sheets)
2. Include these metrics:
   - Total Revenue (with trend)
   - Active Customers (monthly)
   - Average Order Value
   - Top 5 Products by Revenue
3. Take a screenshot and save as: `dashboard.png` (or .jpg)
4. Optional: Include your dashboard code in `dashboard/`

### Example with Streamlit:
```python
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Cartly Executive Dashboard")

# Load data
orders = pd.read_csv('data/orders.csv')

# KPI row
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"${orders['total'].sum():,.0f}")
col2.metric("Active Customers", orders['customer_id'].nunique())
col3.metric("Avg Order Value", f"${orders['total'].mean():.2f}")

# Charts...
```

### Test locally:
```bash
pytest tests/test_3_4.py -v
```

### Evaluation:
AI vision review of dashboard screenshot.

---

## Tips for Week 3

- **Start with the question** - What business problem are you solving?
- **Tell a story** - Your analysis should have a narrative
- **Visualize thoughtfully** - Choose the right chart for the data
- **Cite your data** - Show the numbers that support your conclusions
- **Think about your audience** - Meera doesn't want technical jargon

You're halfway through the internship. Keep pushing!
