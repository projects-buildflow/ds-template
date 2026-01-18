# Task 4.2: Implement Pipeline

| XP Reward | Estimated Time | Type |
|-----------|----------------|------|
| 125 XP | 120 min | PR with automated tests |

**Prerequisite:** [Task 4.1: Pipeline Architecture](../task-4.1/INSTRUCTIONS.md)

## Quick Links

- [GitHub Repository](https://github.com/cartly-data/{your-cohort-repo})
- [Discord #ask-priya](https://discord.com/channels/cartly/ask-priya) - Get help
- [All Tasks Overview](../../docs/)


## Objective

Build the data pipeline you designed in Task 4.1.

## Steps

1. **Create your pipeline folder structure**

   ```
   cohort/{your-github-username}/week-4/pipeline/
   ├── extract.py       # Data extraction functions
   ├── transform.py     # Data transformation functions
   ├── load.py          # Data loading functions
   ├── run_pipeline.py  # Main pipeline orchestrator
   ├── config.py        # Configuration settings
   └── tests/
       └── test_pipeline.py
   ```

2. **Implement each component**

3. **Make it runnable**
   ```bash
   python run_pipeline.py
   ```

## Requirements

- Pipeline should run via `python run_pipeline.py`
- Should handle errors gracefully (don't crash on bad data)
- Should log activities using Python's logging module
- Include docstrings for all functions
- Include tests that verify the pipeline works

## Example: run_pipeline.py

```python
"""Main pipeline orchestrator for daily analytics."""

import logging
from extract import extract_orders, extract_customers
from transform import clean_orders, aggregate_daily_revenue
from load import save_to_csv

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def run_pipeline():
    """Execute the full data pipeline."""
    logger.info("Starting daily analytics pipeline...")

    try:
        # Extract
        logger.info("Extracting data...")
        orders = extract_orders()
        customers = extract_customers()
        logger.info(f"Extracted {len(orders)} orders, {len(customers)} customers")

        # Transform
        logger.info("Transforming data...")
        clean_orders_df = clean_orders(orders)
        daily_revenue = aggregate_daily_revenue(clean_orders_df)

        # Load
        logger.info("Loading results...")
        save_to_csv(daily_revenue, "output/daily_revenue.csv")

        logger.info("Pipeline completed successfully!")

    except Exception as e:
        logger.error(f"Pipeline failed: {e}", exc_info=True)
        raise


if __name__ == "__main__":
    run_pipeline()
```

## Example: config.py

```python
"""Configuration settings for the pipeline."""

from pathlib import Path

# Paths
BASE_DIR = Path(__file__).parent.parent.parent.parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = Path(__file__).parent / "output"

# Files
ORDERS_FILE = DATA_DIR / "orders.csv"
CUSTOMERS_FILE = DATA_DIR / "customers.csv"

# Ensure output directory exists
OUTPUT_DIR.mkdir(exist_ok=True)
```

## Test Locally

```bash
# Run your pipeline
cd cohort/{your-github-username}/week-4/pipeline
python run_pipeline.py

# Run automated tests
pytest tests/test_4_2.py -v --student-folder=cohort/{your-github-username}
```


## How to Submit

1. **Create a branch:**
   ```bash
   git checkout -b task-4.2-{your-github-username}
   ```

2. **Do your work** in `cohort/{your-github-username}/`

3. **Test locally:**
   ```bash
   pytest tests/test_4_2.py -v
   ```

4. **Commit and push:**
   ```bash
   git add .
   git commit -m "Complete task 4.2"
   git push -u origin task-4.2-{your-github-username}
   ```

5. **Open a Pull Request** on GitHub and wait for CI to pass

## Tips

- Start simple - get a basic version working first
- Add error handling incrementally
- Use relative imports within your pipeline package
- Test each component before connecting them

## Evaluation

Automated tests will verify:
- Required files exist
- Pipeline can be imported
- Pipeline runs without errors
- Output is generated correctly


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
**Previous Task:** [Task 4.1: Pipeline Architecture](../task-4.1/INSTRUCTIONS.md) | **Next Task:** [Task 4.3: Debug AI Code](../task-4.3/INSTRUCTIONS.md)
