# Week 2: Data Quality

Welcome to Week 2! Now that you've got your environment set up, it's time to dive into data quality - the foundation of good analytics.

---

## Task 2.1: Data Profiling Report (75 XP)

**Objective:** Create a comprehensive data profiling report for our customer dataset.

### The Situation:
Priya noticed some anomalies in last week's analytics report. Before we can trust the data, we need to understand it better. She wants you to profile the dataset and identify any quality issues.

### Steps:
1. Load the customer data from `data/customers.csv`
2. Create a Jupyter notebook: `data_profile.ipynb`
3. Include the following sections:
   - **Data Overview**: Row count, column types, memory usage
   - **Missing Values**: Which columns have nulls? What percentage?
   - **Distributions**: Numeric columns stats, categorical value counts
   - **Outliers**: Identify any suspicious values
   - **Recommendations**: What should be cleaned or investigated?

### Example:
```python
import pandas as pd
import numpy as np

def profile_dataframe(df):
    """Generate a basic profile of the DataFrame."""
    profile = {
        'rows': len(df),
        'columns': len(df.columns),
        'missing_values': df.isnull().sum().to_dict(),
        # Add more...
    }
    return profile
```

### Test locally:
```bash
pytest tests/test_2_1.py -v
```

### Evaluation:
PR-based with automated notebook checks.

---

## Task 2.2: Validation Schema with Pandera (75 XP)

**Objective:** Create a data validation schema using Pandera.

### The Situation:
After your profiling report, the team decided we need automated data validation. Create a Pandera schema that can validate incoming customer data.

### Steps:
1. Install Pandera if needed: `pip install pandera`
2. Create: `validation_schema.py`
3. Define a schema that validates:
   - `customer_id`: Positive integers, unique
   - `email`: Valid email format (contains @)
   - `age`: Between 18 and 120 (or null)
   - `total_orders`: Non-negative integers
   - `total_spent`: Non-negative floats

### Example:
```python
import pandera as pa
from pandera import Column, Check

customer_schema = pa.DataFrameSchema({
    "customer_id": Column(int, Check.greater_than(0), unique=True),
    "email": Column(str, Check.str_contains("@")),
    # Add more columns...
})
```

### Test locally:
```bash
pytest tests/test_2_2.py -v
```

### Evaluation:
PR-based with automated tests.

---

## Task 2.3: Data Cleaning Pipeline (100 XP)

**Objective:** Build a reusable data cleaning pipeline.

### The Situation:
We receive customer data from multiple sources with varying quality. Build a cleaning pipeline that can standardize and clean this data.

### Steps:
1. Create: `cleaning_pipeline.py`
2. Implement a `DataCleaningPipeline` class with these methods:
   - `standardize_emails(df)`: Lowercase all emails
   - `handle_missing_ages(df)`: Fill missing ages with median
   - `remove_invalid_orders(df)`: Remove rows where `total_orders < 0`
   - `clean(df)`: Run all cleaning steps in order
3. Each method should return a new DataFrame (don't modify in place)

### Example:
```python
import pandas as pd

class DataCleaningPipeline:
    """Pipeline for cleaning customer data."""

    def standardize_emails(self, df: pd.DataFrame) -> pd.DataFrame:
        """Convert all emails to lowercase."""
        result = df.copy()
        result['email'] = result['email'].str.lower()
        return result

    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        """Run all cleaning steps."""
        df = self.standardize_emails(df)
        df = self.handle_missing_ages(df)
        df = self.remove_invalid_orders(df)
        return df
```

### Test locally:
```bash
pytest tests/test_2_3.py -v
```

### Evaluation:
PR-based with automated tests.

---

## Task 2.4: Code Review Guidelines (50 XP)

**Objective:** Create a code review checklist for data cleaning pipelines.

### The Situation:
> **Priya:** "You've built a solid data cleaning pipeline. Now I want you to document what makes good data cleaning code. Create a review checklist that we can use when reviewing each other's data pipelines."

### Steps:
1. Create: `code_review_checklist.md`
2. Create a comprehensive checklist covering:
   - **Correctness**: Does the code actually clean the data properly?
   - **Robustness**: Does it handle edge cases and errors?
   - **Readability**: Can other team members understand it?
   - **Performance**: Is it efficient enough for production data?
   - **Testing**: How do we know it works?
3. Include at least 15 specific, actionable checklist items
4. Add a "Common Issues" section with 3+ examples

### Example items:
- "Does the cleaning function return a new DataFrame or modify in place?"
- "Are null values handled before operations that would fail on nulls?"
- "Is there a check for duplicate records after cleaning?"

### Test locally:
```bash
pytest tests/test_2_4.py -v
```

### Evaluation:
PR-based with content validation.

---

## Tips for Week 2

- **Data quality matters** - Bad data leads to bad decisions
- **Test edge cases** - What happens with empty DataFrames? Null values?
- **Document assumptions** - Future you will thank present you
- **Use assertions** - `assert` statements make your assumptions explicit

Keep up the great work!
