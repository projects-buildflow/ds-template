# Task 2.1: Data Profiling Report

| XP Reward | Estimated Time | Type |
|-----------|----------------|------|
| 75 XP | 60 min | PR with notebook review |

**Prerequisite:** [Task 1.4: Document the Fix](../../week-1/task-1.4/INSTRUCTIONS.md)

## Quick Links

- Your repository on GitHub
- Team Chat - Get help from mentors
- [All Tasks Overview](../../docs/)


## Objective

Create a comprehensive data profiling report for our customer dataset.

## The Situation

Priya noticed some anomalies in last week's analytics report. Before we can trust the data, we need to understand it better. She wants you to profile the dataset and identify any quality issues.

## Steps

1. **Load the data**
   ```python
   import pandas as pd
   customers = pd.read_csv('data/customers.csv')
   ```

2. **Create your notebook**

   Create: `data_profile.ipynb`

3. **Include these sections:**

   - **Data Overview**: Row count, column types, memory usage
   - **Missing Values**: Which columns have nulls? What percentage?
   - **Distributions**: Numeric columns stats, categorical value counts
   - **Outliers**: Identify any suspicious values
   - **Recommendations**: What should be cleaned or investigated?

## Example Code

```python
import pandas as pd
import numpy as np

def profile_dataframe(df):
    """Generate a basic profile of the DataFrame."""
    profile = {
        'rows': len(df),
        'columns': len(df.columns),
        'missing_values': df.isnull().sum().to_dict(),
        'dtypes': df.dtypes.to_dict(),
    }
    return profile

# Your analysis here...
```

## Test Locally

```bash
pytest tests/test_2_1.py -v
```


## How to Submit

1. **Create a branch:**
   ```bash
   git checkout -b task-2.1
   ```

2. **Do your work** in the repository root

3. **Test locally:**
   ```bash
   pytest tests/test_2_1.py -v
   ```

4. **Commit and push:**
   ```bash
   git add .
   git commit -m "Complete task 2.1"
   git push -u origin task-2.1
   ```

5. **Open a Pull Request** on GitHub and wait for CI to pass

## Tips

- Use visualizations to make your findings clear
- Be specific about what you find - "there are outliers" is less useful than "5 customers have ages over 100"
- Think about what each issue means for downstream analysis

## Evaluation

Your notebook will be reviewed for completeness and insight quality.


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
**Previous Task:** [Task 1.4: Document the Fix](../../week-1/task-1.4/INSTRUCTIONS.md) | **Next Task:** [Task 2.2: Write Validation Rules](../task-2.2/INSTRUCTIONS.md)
