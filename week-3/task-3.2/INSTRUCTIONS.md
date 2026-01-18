# Task 3.2: SQL Cohort Analysis

| XP Reward | Estimated Time | Type |
|-----------|----------------|------|
| 75 XP | 60 min | PR with SQL execution tests |

**Prerequisite:** [Task 3.1: Revenue Investigation](../task-3.1/INSTRUCTIONS.md)

## Quick Links

- [GitHub Repository](https://github.com/cartly-data/{your-cohort-repo})
- [Discord #ask-priya](https://discord.com/channels/cartly/ask-priya) - Get help
- [All Tasks Overview](../../docs/)


## Objective

Build a customer retention cohort analysis using SQL.

## The Situation

Vikram (Product Manager) wants to understand customer retention patterns. He needs a cohort analysis showing how many customers return each month after their first purchase.

## Steps

1. **Create your SQL file**

   Create: `cohort/{your-github-username}/week-3/cohort_analysis.sql`

2. **Write a query that:**
   - Groups customers by their first purchase month (their "cohort")
   - Shows retention for months 0, 1, 2, 3, 4, 5
   - Uses standard SQL (SQLite or PostgreSQL syntax)

## Expected Output Format

| cohort_month | month_0 | month_1 | month_2 | month_3 | month_4 | month_5 |
|--------------|---------|---------|---------|---------|---------|---------|
| 2024-01      | 100     | 45      | 32      | 28      | 25      | 22      |
| 2024-02      | 120     | 52      | 38      | 30      | 27      | NULL    |
| ...          | ...     | ...     | ...     | ...     | ...     | ...     |

## Approach

```sql
-- Step 1: Find each customer's cohort (first purchase month)
WITH customer_cohorts AS (
    SELECT
        customer_id,
        DATE_TRUNC('month', MIN(order_date)) AS cohort_month
    FROM orders
    GROUP BY customer_id
),

-- Step 2: Join orders with cohorts and calculate months since first purchase
cohort_orders AS (
    SELECT
        c.cohort_month,
        o.customer_id,
        DATE_TRUNC('month', o.order_date) AS order_month,
        -- Calculate months since cohort month
        -- (implementation depends on your SQL dialect)
    FROM orders o
    JOIN customer_cohorts c ON o.customer_id = c.customer_id
)

-- Step 3: Pivot to get retention by month
SELECT
    cohort_month,
    COUNT(DISTINCT CASE WHEN months_since_first = 0 THEN customer_id END) AS month_0,
    COUNT(DISTINCT CASE WHEN months_since_first = 1 THEN customer_id END) AS month_1,
    -- ... continue for other months
FROM cohort_orders
GROUP BY cohort_month
ORDER BY cohort_month;
```

## Test Locally

```bash
pytest tests/test_3_2.py -v --student-folder=cohort/{your-github-username}
```


## How to Submit

1. **Create a branch:**
   ```bash
   git checkout -b task-3.2-{your-github-username}
   ```

2. **Do your work** in `cohort/{your-github-username}/`

3. **Test locally:**
   ```bash
   pytest tests/test_3_2.py -v
   ```

4. **Commit and push:**
   ```bash
   git add .
   git commit -m "Complete task 3.2"
   git push -u origin task-3.2-{your-github-username}
   ```

5. **Open a Pull Request** on GitHub and wait for CI to pass

## Tips

- month_0 is the cohort size (customers who made their first purchase)
- Each subsequent month shows how many returned
- Use CTEs (WITH clauses) to break down the problem
- Test your query with a small date range first

## Evaluation

Your query will be executed and the output format validated.


## Common Errors

**"ModuleNotFoundError"**
- Ensure your virtual environment is activated: `source venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt`

**"FileNotFoundError"**
- Check you're in the repository root directory
- Verify the file path matches exactly (case-sensitive)

**Tests failing locally but code looks correct**
- Check for trailing whitespace or formatting issues
- Run `black` and `ruff` to auto-fix style issues

**Still stuck?** Ask in `#ask-priya` on Discord!

---
**Previous Task:** [Task 3.1: Revenue Investigation](../task-3.1/INSTRUCTIONS.md) | **Next Task:** [Task 3.3: Query Optimization](../task-3.3/INSTRUCTIONS.md)
