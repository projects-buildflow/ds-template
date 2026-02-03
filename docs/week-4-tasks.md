# Week 4: Capstone

"Prove you're ready. Build something real."

Welcome to your final week! You've learned the fundamentals. Now it's time to put it all together and build a production-quality data pipeline.

---

## Task 4.1: Pipeline Architecture (100 XP)

**Objective:** Design the architecture for a data pipeline.

### The Situation:
Priya wants to automate the daily analytics workflow. Currently, someone manually runs scripts every morning. Your job: design a pipeline that can run unattended.

### Steps:
1. Create: `pipeline_design.md`
2. Include these sections:
   - **Overview**: What does the pipeline do? (1-2 paragraphs)
   - **Data Flow**: Diagram or description of data movement
   - **Components**: List each component and its responsibility
   - **Error Handling**: How will errors be caught and reported?
   - **Monitoring**: How will you know if it's working?
   - **Technology Choices**: What tools/libraries and why?

### Requirements:
The pipeline should:
- Extract data from CSV files (simulating external sources)
- Transform: clean, validate, and aggregate
- Load: save to processed output files
- Be idempotent (safe to re-run)
- Log its activities

### Example structure:
```markdown
# Daily Analytics Pipeline - Design Document

## Overview
This pipeline processes daily order data from Cartly's e-commerce platform...

## Data Flow
```
[CSV Files] → [Extract] → [Validate] → [Transform] → [Aggregate] → [Output]
                 ↓            ↓             ↓
              [Logs]      [Errors]     [Metrics]
```

## Components
1. **Extractor**: Reads CSV files from data/ directory
   - Handles missing files gracefully
   - Validates file format before processing
...
```

### Test locally:
```bash
pytest tests/test_4_1.py -v
```

### Evaluation:
PR-based with document review for completeness.

---

## Task 4.2: Implement Pipeline (125 XP)

**Objective:** Build the pipeline you designed.

### The Situation:
Time to bring your design to life! Implement a working data pipeline.

### Steps:
1. Create this folder structure:
   ```
   pipeline/
   ├── extract.py       # Data extraction functions
   ├── transform.py     # Data transformation functions
   ├── load.py          # Data loading functions
   ├── run_pipeline.py  # Main pipeline orchestrator
   ├── config.py        # Configuration settings
   └── tests/           # Your pipeline tests
       └── test_pipeline.py
   ```

2. Implement each component:
   - `extract.py`: Functions to read source data
   - `transform.py`: Cleaning, validation, aggregation
   - `load.py`: Write processed data to output
   - `run_pipeline.py`: Orchestrate the full flow
   - `config.py`: Paths, settings, constants

3. Requirements:
   - Pipeline should be runnable via: `python run_pipeline.py`
   - Should handle errors gracefully (don't crash on bad data)
   - Should log activities (use Python's logging module)
   - Include docstrings for all functions

### Example:
```python
# run_pipeline.py
import logging
from extract import extract_orders, extract_customers
from transform import clean_orders, aggregate_daily_revenue
from load import save_to_csv

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_pipeline():
    """Execute the full data pipeline."""
    logger.info("Starting pipeline...")

    # Extract
    orders = extract_orders()
    customers = extract_customers()

    # Transform
    clean_orders_df = clean_orders(orders)
    daily_revenue = aggregate_daily_revenue(clean_orders_df)

    # Load
    save_to_csv(daily_revenue, "output/daily_revenue.csv")

    logger.info("Pipeline complete!")

if __name__ == "__main__":
    run_pipeline()
```

### Test locally:
```bash
pytest tests/test_4_2.py -v
```

### Evaluation:
PR-based with automated tests and code review.

---

## Task 4.3: Debug AI Code (75 XP)

**Objective:** Find and fix bugs in AI-generated code.

### The Situation:
A junior developer used AI to generate a data validator, but it has bugs. Your job: find the bugs, fix them, and document what you found.

### Steps:
1. Look at `week-4/task-4.3/ai_generated_validator.py`
2. Create: `fixed_validator.py` (corrected version)
3. Create: `bug_report.md` documenting:
   - Each bug you found
   - What was wrong
   - How you fixed it

### The validator has exactly 5 bugs. Can you find them all?

### Hints:
- Test with edge cases (empty strings, boundary values)
- Look carefully at comparison operators
- Check regex patterns
- Consider logical operators

### Example bug_report.md:
```markdown
# Bug Report: AI-Generated Validator

## Bug 1: Off-by-one error in age validation
**Location**: Line 15
**Problem**: Uses `> 120` instead of `>= 120`
**Impact**: Allows age 120 which should be invalid
**Fix**: Changed to `>= 120`

## Bug 2: ...
```

### Test locally:
```bash
pytest tests/test_4_3.py -v
```

### Evaluation:
PR-based with automated tests against edge cases.

---

## Task 4.4: Final Presentation (150 XP)

**Objective:** Present your internship work to the team.

### The Situation:
It's your last day! Priya has asked you to present your work to the team. This is your chance to showcase what you've learned.

### Steps:
1. Create a presentation (PDF format): `presentation.pdf`
2. Include these sections:
   - **Introduction**: Who you are, your background (1 slide)
   - **Journey**: Your path through the internship (1-2 slides)
   - **Key Project**: Deep dive into your best work (2-3 slides)
   - **Learnings**: What you learned, challenges overcome (1 slide)
   - **Future**: What you want to learn next (1 slide)

### Requirements:
- 6-10 slides total
- Include at least one data visualization
- Keep text minimal - use bullet points
- Include speaker notes or a separate script

### Tips:
- Lead with impact: "I built X which does Y"
- Show, don't tell: Include screenshots, code snippets, charts
- Be specific: Numbers and metrics are compelling
- Practice: Run through it once before submitting

### Example first slide:
```
MY DATA INTERNSHIP JOURNEY
{your-name}

Week 1: Built data cleaning pipeline
Week 2: Created validation system
Week 3: Investigated revenue drop → found root cause
Week 4: Built automated analytics pipeline

Key Achievement: Reduced manual reporting time by 80%
```

### Test locally:
```bash
pytest tests/test_4_4.py -v
```

### Evaluation:
AI-powered presentation review.

---

## Congratulations!

If you've made it here, you've completed the Cartly Data Internship. You should be proud!

### What you've accomplished:
- Set up a professional development environment
- Written production-quality data cleaning code
- Built data validation systems
- Conducted business analysis
- Optimized SQL queries
- Created dashboards
- Designed and built a data pipeline
- Debugged code and documented your work
- Presented your work professionally

### What's next?
- Connect with your peers on LinkedIn
- Add this project to your portfolio
- Keep building! The best way to learn is to do.

Thank you for being part of Cartly. Good luck with your data career!

*— The Cartly Team*
