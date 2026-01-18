# Task 1.3: Fix the Date Bug

| XP Reward | Estimated Time | Type |
|-----------|----------------|------|
| 50 XP | 30 min | PR with automated tests |

**Prerequisite:** [Task 1.2: Join the Team](../task-1.2/INSTRUCTIONS.md)

## Quick Links

- [GitHub Repository](https://github.com/cartly-data/{your-cohort-repo})
- [Discord #ask-priya](https://discord.com/channels/cartly/ask-priya) - Get help
- [All Tasks Overview](../../docs/)


## Objective

Fix a bug in the data loading module that causes dates to parse incorrectly.

## The Situation

The `src/data_loader.py` module has a bug in the `load_orders()` function. When loading order data, dates are being parsed incorrectly, resulting in NaT (Not a Time) values or wrong dates.

## Steps

1. **Examine the bug**

   Look at `src/data_loader.py` and find the issue in the `load_orders()` function.

2. **Understand the data**

   Check `data/orders.csv` (or `data/sample_orders.csv`) to see the actual date format used.

3. **Fix the bug**

   Create a corrected version of the data loader or document the fix.

4. **Create documentation**

   Create `cohort/{your-github-username}/week-1/README.md` explaining:
   - What the bug was
   - How you fixed it
   - Why the fix works

## The Bug

The `load_orders()` function specifies a date format that doesn't match the actual data format. This causes pandas to fail when parsing dates.

## Test Locally

```bash
pytest tests/test_1_3.py -v --student-folder=cohort/{your-github-username}
```

## Hints

- Look at the `date_format` parameter in `pd.read_csv()`
- Check what format the CSV dates are actually in
- Sometimes letting pandas infer the date format works best

## Evaluation

Submit your PR with your README explaining the fix. The tests will verify that dates parse correctly.


## How to Submit

1. **Create a branch:**
   ```bash
   git checkout -b task-1.3-{your-github-username}
   ```

2. **Do your work** in `cohort/{your-github-username}/`

3. **Test locally:**
   ```bash
   pytest tests/test_1_3.py -v
   ```

4. **Commit and push:**
   ```bash
   git add .
   git commit -m "Complete task 1.3"
   git push -u origin task-1.3-{your-github-username}
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
**Previous Task:** [Task 1.2: Join the Team](../task-1.2/INSTRUCTIONS.md) | **Next Task:** [Task 1.4: Document the Fix](../task-1.4/INSTRUCTIONS.md)
