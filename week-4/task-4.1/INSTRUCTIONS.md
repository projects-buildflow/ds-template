# Task 4.1: Pipeline Architecture

| XP Reward | Estimated Time | Type |
|-----------|----------------|------|
| 100 XP | 60 min | PR with document review |

**Prerequisite:** [Task 3.4: Dashboard Creation](../../week-3/task-3.4/INSTRUCTIONS.md)

## Quick Links

- Your repository on GitHub
- Team Chat - Get help from mentors
- [All Tasks Overview](../../docs/)


## Objective

Design the architecture for an automated data pipeline.

## The Situation

Priya wants to automate the daily analytics workflow. Currently, someone manually runs scripts every morning. Your job: design a pipeline that can run unattended.

## Steps

1. **Create your design document**

   Create: `pipeline_design.md`

2. **Include these sections:**

   - **Overview**: What does the pipeline do? (1-2 paragraphs)
   - **Data Flow**: Diagram or description of data movement
   - **Components**: List each component and its responsibility
   - **Error Handling**: How will errors be caught and reported?
   - **Monitoring**: How will you know if it's working?
   - **Technology Choices**: What tools/libraries and why?

## Pipeline Requirements

Your pipeline design should:
- Extract data from CSV files (simulating external sources)
- Transform: clean, validate, and aggregate
- Load: save to processed output files
- Be idempotent (safe to re-run)
- Log its activities

## Example Structure

```markdown
# Daily Analytics Pipeline - Design Document

## Overview

This pipeline processes daily order data from Cartly's e-commerce platform,
cleaning and aggregating it for the analytics team. It runs automatically
each morning and produces daily revenue reports and customer metrics.

## Data Flow

```
[CSV Files] → [Extract] → [Validate] → [Transform] → [Aggregate] → [Output]
                 ↓            ↓             ↓
              [Logs]      [Errors]     [Metrics]
```

## Components

### 1. Extractor
- Reads CSV files from the `data/` directory
- Handles missing files gracefully
- Validates file format before processing

### 2. Validator
- Checks data against Pandera schema
- Quarantines invalid records
- Logs validation failures

### 3. Transformer
- Cleans data (standardize emails, handle nulls)
- Applies business rules
- Creates derived fields

### 4. Aggregator
- Calculates daily metrics
- Generates summary tables
- Computes trends

### 5. Loader
- Writes output to processed/ directory
- Creates dated files for auditing
- Updates "latest" symlinks

## Error Handling

- Invalid records are logged and quarantined, not dropped silently
- If a file is missing, pipeline logs warning and continues with available data
- Critical failures (can't write output) send alert to #data-alerts channel
- All errors are logged with stack traces

## Monitoring

- Each run creates a log file with timestamp
- Summary metrics logged: records processed, errors, runtime
- Output directory has manifest file listing all generated files

## Technology Choices

- **Python 3.10+**: Team's primary language
- **Pandas**: Data manipulation
- **Pandera**: Data validation
- **Logging module**: Standard Python logging
- **Pathlib**: File path handling
```

## Test Locally

```bash
pytest tests/test_4_1.py -v
```


## How to Submit

1. **Create a branch:**
   ```bash
   git checkout -b task-4.1
   ```

2. **Do your work** in the repository root

3. **Test locally:**
   ```bash
   pytest tests/test_4_1.py -v
   ```

4. **Commit and push:**
   ```bash
   git add .
   git commit -m "Complete task 4.1"
   git push -u origin task-4.1
   ```

5. **Open a Pull Request** on GitHub and wait for CI to pass

## Tips

- Think about what can go wrong and how you'll handle it
- Consider maintainability - will someone else understand this?
- Be specific about technology choices and justify them
- Draw diagrams if it helps explain the flow

## Evaluation

Your design document will be reviewed for completeness and thoughtfulness.


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
**Previous Task:** [Task 3.4: Dashboard Creation](../../week-3/task-3.4/INSTRUCTIONS.md) | **Next Task:** [Task 4.2: Implement Pipeline](../task-4.2/INSTRUCTIONS.md)
