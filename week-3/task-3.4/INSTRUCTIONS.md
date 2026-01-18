# Task 3.4: Dashboard Creation

| XP Reward | Estimated Time | Type |
|-----------|----------------|------|
| 100 XP | 90 min | AI vision review |

**Prerequisite:** [Task 3.3: Query Optimization](../task-3.3/INSTRUCTIONS.md)

## Quick Links

- [GitHub Repository](https://github.com/cartly-data/{your-cohort-repo})
- [Discord #ask-priya](https://discord.com/channels/cartly/ask-priya) - Get help
- [All Tasks Overview](../../docs/)


## Objective

Create a business dashboard for the executive team.

## The Situation

Meera loved your revenue analysis! Now she wants a dashboard the team can check weekly. Create a dashboard showing key business metrics.

## Steps

1. **Choose your tool**

   You can use any tool:
   - Streamlit (recommended for Python)
   - Dash (Plotly)
   - Google Sheets/Data Studio
   - Metabase
   - Even a well-designed Jupyter notebook with widgets

2. **Include these metrics:**
   - **Total Revenue** (with trend indicator)
   - **Active Customers** (monthly)
   - **Average Order Value**
   - **Top 5 Products by Revenue**

3. **Save a screenshot**

   Save as: `cohort/{your-github-username}/week-3/dashboard.png` (or .jpg)

4. **Optional: Include code**

   If using code, save in: `cohort/{your-github-username}/week-3/dashboard/`

## Example with Streamlit

```python
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Cartly Executive Dashboard")

# Load data
orders = pd.read_csv('../../data/orders.csv', parse_dates=['order_date'])
products = pd.read_csv('../../data/products.csv')

# KPI Row
col1, col2, col3 = st.columns(3)

total_revenue = orders['total'].sum()
active_customers = orders['customer_id'].nunique()
avg_order_value = orders['total'].mean()

col1.metric("Total Revenue", f"${total_revenue:,.0f}", "+12%")
col2.metric("Active Customers", f"{active_customers:,}")
col3.metric("Avg Order Value", f"${avg_order_value:.2f}")

# Revenue Trend Chart
st.subheader("Revenue Trend")
monthly = orders.groupby(orders['order_date'].dt.to_period('M'))['total'].sum()
fig = px.line(x=monthly.index.astype(str), y=monthly.values)
st.plotly_chart(fig)

# Top Products
st.subheader("Top 5 Products by Revenue")
# ... your code here
```

## Test Locally

```bash
pytest tests/test_3_4.py -v --student-folder=cohort/{your-github-username}
```

## Dashboard Best Practices

1. **Keep it simple** - Less is more for executive dashboards
2. **Use clear labels** - No jargon or ambiguous abbreviations
3. **Choose appropriate charts** - Bar for comparisons, line for trends
4. **Include context** - Show comparisons (vs. last month, vs. target)
5. **Make it scannable** - Key metrics should be visible at a glance

## Tips

- Focus on insights, not raw data
- Use color intentionally (red for bad, green for good)
- Make sure text is readable in the screenshot
- Test with someone unfamiliar with the data - can they understand it?

## Evaluation

Your dashboard screenshot will be reviewed by AI vision for:
- Required metrics present
- Clear and readable design
- Appropriate visualizations


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
**Previous Task:** [Task 3.3: Query Optimization](../task-3.3/INSTRUCTIONS.md) | **Next Task:** [Task 4.1: Pipeline Architecture](../../week-4/task-4.1/INSTRUCTIONS.md)
