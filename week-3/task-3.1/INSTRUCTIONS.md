# Task 3.1: Revenue Investigation

| XP Reward | Estimated Time | Type |
|-----------|----------------|------|
| 100 XP | 90 min | AI-reviewed notebook |

**Prerequisite:** [Task 2.4: Code Review Guidelines](../../week-2/task-2.4/INSTRUCTIONS.md)

## Quick Links

- [GitHub Repository](https://github.com/cartly-data/{your-cohort-repo})
- [Discord #ask-priya](https://discord.com/channels/cartly/ask-priya) - Get help
- [All Tasks Overview](../../docs/)


## Objective

Investigate why revenue dropped and present your findings to the executive team.

## The Situation

Meera (CEO) just sent an urgent Slack message:

> "Revenue is down 15% this month. I need to understand why before the board meeting next week."

Priya has assigned this to you. Time to put your analysis skills to work.

## Steps

1. **Create your notebook**

   Create: `cohort/{your-github-username}/week-3/revenue_investigation.ipynb`

2. **Load and analyze the data**
   ```python
   import pandas as pd
   orders = pd.read_csv('../../data/orders.csv')
   customers = pd.read_csv('../../data/customers.csv')
   ```

3. **Include these required sections:**

   - **Executive Summary**: Key finding in 2-3 sentences
   - **Analysis**: Charts and tables supporting your findings
   - **Root Cause**: What's causing the revenue drop?
   - **Recommendations**: 2-3 actionable suggestions

## Analysis Hints

- Look at order volume vs. average order value
- Check for changes in customer segments
- Consider seasonal patterns
- Compare different time periods
- Don't just describe *what* happened - explain *why*

## Example Structure

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

orders = pd.read_csv('../../data/orders.csv', parse_dates=['order_date'])

# Monthly revenue trend
monthly_revenue = orders.groupby(orders['order_date'].dt.to_period('M'))['total'].sum()
monthly_revenue.plot(kind='bar')
plt.title('Monthly Revenue')
plt.show()

# More analysis...
```

## Test Locally

```bash
pytest tests/test_3_1.py -v --student-folder=cohort/{your-github-username}
```

## Tips

- Lead with your conclusion, then show supporting evidence
- Use visualizations to make your points clear
- Be specific: "revenue dropped 15%" is better than "revenue went down"
- Think about your audience - Meera wants actionable insights, not technical details

## Evaluation

Your notebook will be reviewed by AI for completeness and insight quality.


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
**Previous Task:** [Task 2.4: Code Review Guidelines](../../week-2/task-2.4/INSTRUCTIONS.md) | **Next Task:** [Task 3.2: SQL Cohort Analysis](../task-3.2/INSTRUCTIONS.md)
