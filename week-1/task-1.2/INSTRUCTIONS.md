# Task 1.2: Your First Bug Fix

| XP Reward | Estimated Time | Type |
|-----------|----------------|------|
| 50 XP | 30 min | PR with automated tests |

**Prerequisite:** [Task 1.1: Environment Setup](../task-1.1/INSTRUCTIONS.md)

## Quick Links

- [GitHub Repository](https://github.com/cartly-data/{your-cohort-repo})
- [Discord #ask-priya](https://discord.com/channels/cartly/ask-priya) - Get help
- [All Tasks Overview](../../docs/)


## Objective

Fix a bug in the data cleaning script.

## The Situation

Ananya from the Analytics team found that our customer deduplication isn't working. The `remove_duplicates()` function should identify duplicate customers by email (case-insensitive), but it's not catching all duplicates.

## Steps

1. **Look at the data**

   Open `data/customers.csv` and notice there are duplicate entries for "Rahul Kumar" and "Priya Sharma" with slightly different email casings (e.g., `RAHUL.KUMAR@email.com` vs `rahul.kumar@email.com`).

2. **Create your solution file**

   Create: `cohort/{your-github-username}/week-1/clean_data.py`

3. **Implement the function**

   ```python
   import pandas as pd

   def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
       """
       Remove duplicate customers based on email (case-insensitive).
       Keep the record with the highest total_orders.

       Args:
           df: DataFrame with customer data

       Returns:
           DataFrame with duplicates removed
       """
       # Your code here
       pass
   ```

## Requirements

Your function should:
- Take a pandas DataFrame as input
- Identify duplicates by email (case-insensitive comparison)
- When duplicates exist, keep only the record with the highest `total_orders`
- Return a new DataFrame with duplicates removed

## Test Locally

```bash
pytest tests/test_1_2.py -v --student-folder=cohort/{your-github-username}
```

## Hints

- Use `.str.lower()` to normalize email casing
- Check out `df.sort_values()` and `df.drop_duplicates()`
- Remember to handle the case where there are no duplicates

## Evaluation

Submit your PR. Automated tests will verify your implementation.


## How to Submit

1. **Create a branch:**
   ```bash
   git checkout -b task-1.2-{your-github-username}
   ```

2. **Do your work** in `cohort/{your-github-username}/`

3. **Test locally:**
   ```bash
   pytest tests/test_1_2.py -v
   ```

4. **Commit and push:**
   ```bash
   git add .
   git commit -m "Complete task 1.2"
   git push -u origin task-1.2-{your-github-username}
   ```

5. **Open a Pull Request** on GitHub and wait for CI to pass


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
**Previous Task:** [Task 1.1: Environment Setup](../task-1.1/INSTRUCTIONS.md) | **Next Task:** [Task 1.3: Fix the Date Bug](../task-1.3/INSTRUCTIONS.md)
