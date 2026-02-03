# Task 3.3: Query Optimization

| XP Reward | Estimated Time | Type |
|-----------|----------------|------|
| 75 XP | 45 min | PR with output comparison |

**Prerequisite:** [Task 3.2: SQL Cohort Analysis](../task-3.2/INSTRUCTIONS.md)

## Quick Links

- Your repository on GitHub
- Team Chat - Get help from mentors
- [All Tasks Overview](../../docs/)


## Objective

Optimize a slow SQL query without changing its results.

## The Situation

Ananya found a query that's taking 30+ seconds to run. It's blocking other reports and needs to be fixed. Your job: make it faster while producing the same results.

## Steps

1. **Review the slow query**

   Look at `week-3/task-3.3/slow_query.sql` to understand what it does.

2. **Create your optimized version**

   Create: `optimized_query.sql`

3. **Document your changes**

   Create: `optimization_notes.md`

   Include:
   - What made the original query slow
   - What changes you made
   - Why your changes improve performance

## Common Optimization Techniques

1. **Remove SELECT ***
   - Only select the columns you need

2. **Eliminate correlated subqueries**
   - Replace with JOINs or CTEs

3. **Use appropriate indexes**
   - Document which indexes would help

4. **Avoid function calls on indexed columns**
   - `DATE(order_date)` prevents index use
   - Better: compare against date ranges

5. **Use window functions**
   - More efficient than self-joins for running calculations

6. **Reduce redundant calculations**
   - Calculate aggregates once, not multiple times

## Example optimization_notes.md

```markdown
# Query Optimization Notes

## Original Problems

1. **Correlated subqueries**: The original query had 6 subqueries that each scanned the orders table separately.

2. **SELECT ***: The outer query selected all columns when only 5 were needed.

3. **DATE() function**: Using DATE(order_date) prevented index usage on the order_date column.

## Changes Made

1. Replaced correlated subqueries with a single CTE that pre-aggregates daily metrics.

2. Specified only the required columns in the final SELECT.

3. Changed date comparisons to use range queries instead of DATE() function.

## Expected Performance Improvement

The optimized query should run in under 1 second compared to 30+ seconds for the original.
```

## Test Locally

```bash
pytest tests/test_3_3.py -v
```


## How to Submit

1. **Create a branch:**
   ```bash
   git checkout -b task-3.3
   ```

2. **Do your work** in the repository root

3. **Test locally:**
   ```bash
   pytest tests/test_3_3.py -v
   ```

4. **Commit and push:**
   ```bash
   git add .
   git commit -m "Complete task 3.3"
   git push -u origin task-3.3
   ```

5. **Open a Pull Request** on GitHub and wait for CI to pass

## Tips

- The output must match the original query's results
- Focus on reducing the number of table scans
- CTEs can make queries both faster AND more readable
- Explain your reasoning - optimization is about understanding why things are slow

## Evaluation

Your optimized query's output will be compared to the original. Your notes will be reviewed for understanding.


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

**Still stuck?** Ask in Team Chat!

---
**Previous Task:** [Task 3.2: SQL Cohort Analysis](../task-3.2/INSTRUCTIONS.md) | **Next Task:** [Task 3.4: Dashboard Creation](../task-3.4/INSTRUCTIONS.md)
