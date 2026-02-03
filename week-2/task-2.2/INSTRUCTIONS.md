# Task 2.2: Validation Schema with Pandera

| XP Reward | Estimated Time | Type |
|-----------|----------------|------|
| 75 XP | 45 min | PR with automated tests |

**Prerequisite:** [Task 2.1: Profile the Marketing Data](../task-2.1/INSTRUCTIONS.md)

## Quick Links

- Your repository on GitHub
- Team Chat - Get help from mentors
- [All Tasks Overview](../../docs/)


## Objective

Create a data validation schema using Pandera to validate incoming customer data.

## The Situation

After your profiling report, the team decided we need automated data validation. Create a Pandera schema that can validate incoming customer data before it enters our analytics pipeline.

## Steps

1. **Install Pandera** (if needed)
   ```bash
   pip install pandera
   ```

2. **Create your schema file**

   Create: `validation_schema.py`

3. **Define validation rules**

   Your schema should validate:
   - `customer_id`: Positive integers, unique
   - `email`: Valid email format (must contain @)
   - `age`: Between 18 and 120 (or null)
   - `total_orders`: Non-negative integers
   - `total_spent`: Non-negative floats

## Example

```python
import pandera as pa
from pandera import Column, Check

customer_schema = pa.DataFrameSchema({
    "customer_id": Column(int, Check.greater_than(0), unique=True),
    "email": Column(str, Check.str_contains("@")),
    "age": Column(float, Check.in_range(18, 120), nullable=True),
    # Add more columns...
})

def validate_customers(df):
    """Validate customer DataFrame against schema."""
    return customer_schema.validate(df)
```

## Test Locally

```bash
pytest tests/test_2_2.py -v
```


## How to Submit

1. **Create a branch:**
   ```bash
   git checkout -b task-2.2
   ```

2. **Do your work** in the repository root

3. **Test locally:**
   ```bash
   pytest tests/test_2_2.py -v
   ```

4. **Commit and push:**
   ```bash
   git add .
   git commit -m "Complete task 2.2"
   git push -u origin task-2.2
   ```

5. **Open a Pull Request** on GitHub and wait for CI to pass

## Tips

- Think about edge cases: What's a valid email? What age range is reasonable?
- Use `nullable=True` for columns that can have missing values
- Consider using custom checks for complex validation logic

## Evaluation

Automated tests will check that your schema correctly accepts valid data and rejects invalid data.


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
**Previous Task:** [Task 2.1: Profile the Marketing Data](../task-2.1/INSTRUCTIONS.md) | **Next Task:** [Task 2.3: Clean the Data](../task-2.3/INSTRUCTIONS.md)
