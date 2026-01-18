# Task 2.3: Data Cleaning Pipeline

| XP Reward | Estimated Time | Type |
|-----------|----------------|------|
| 100 XP | 60 min | PR with automated tests |

**Prerequisite:** [Task 2.2: Write Validation Rules](../task-2.2/INSTRUCTIONS.md)

## Quick Links

- [GitHub Repository](https://github.com/cartly-data/{your-cohort-repo})
- [Discord #ask-priya](https://discord.com/channels/cartly/ask-priya) - Get help
- [All Tasks Overview](../../docs/)


## Objective

Build a reusable data cleaning pipeline that can standardize and clean customer data.

## The Situation

We receive customer data from multiple sources with varying quality. Build a cleaning pipeline that can be run automatically to standardize and clean this data.

## Steps

1. **Create your pipeline file**

   Create: `cohort/{your-github-username}/week-2/cleaning_pipeline.py`

2. **Implement the `DataCleaningPipeline` class**

   Required methods:
   - `standardize_emails(df)`: Lowercase all emails
   - `handle_missing_ages(df)`: Fill missing ages with median
   - `remove_invalid_orders(df)`: Remove rows where `total_orders < 0`
   - `clean(df)`: Run all cleaning steps in order

3. **Requirements**
   - Each method should return a new DataFrame (don't modify in place)
   - The `clean()` method should call all other methods in sequence

## Example

```python
import pandas as pd

class DataCleaningPipeline:
    """Pipeline for cleaning customer data."""

    def standardize_emails(self, df: pd.DataFrame) -> pd.DataFrame:
        """Convert all emails to lowercase."""
        result = df.copy()
        result['email'] = result['email'].str.lower()
        return result

    def handle_missing_ages(self, df: pd.DataFrame) -> pd.DataFrame:
        """Fill missing ages with median age."""
        result = df.copy()
        median_age = result['age'].median()
        result['age'] = result['age'].fillna(median_age)
        return result

    def remove_invalid_orders(self, df: pd.DataFrame) -> pd.DataFrame:
        """Remove rows with negative total_orders."""
        result = df.copy()
        result = result[result['total_orders'] >= 0]
        return result

    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        """Run all cleaning steps in order."""
        df = self.standardize_emails(df)
        df = self.handle_missing_ages(df)
        df = self.remove_invalid_orders(df)
        return df
```

## Test Locally

```bash
pytest tests/test_2_3.py -v --student-folder=cohort/{your-github-username}
```


## How to Submit

1. **Create a branch:**
   ```bash
   git checkout -b task-2.3-{your-github-username}
   ```

2. **Do your work** in `cohort/{your-github-username}/`

3. **Test locally:**
   ```bash
   pytest tests/test_2_3.py -v
   ```

4. **Commit and push:**
   ```bash
   git add .
   git commit -m "Complete task 2.3"
   git push -u origin task-2.3-{your-github-username}
   ```

5. **Open a Pull Request** on GitHub and wait for CI to pass

## Tips

- Always use `.copy()` to avoid modifying the original DataFrame
- Think about the order of operations - does it matter?
- Consider adding logging to track what changes were made

## Evaluation

Automated tests will verify each cleaning method works correctly and that the pipeline runs end-to-end.


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
**Previous Task:** [Task 2.2: Write Validation Rules](../task-2.2/INSTRUCTIONS.md) | **Next Task:** [Task 2.4: Code Review Guidelines](../task-2.4/INSTRUCTIONS.md)
