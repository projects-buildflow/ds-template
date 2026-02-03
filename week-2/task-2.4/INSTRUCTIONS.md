# Task 2.4: Code Review Guidelines

| XP Reward | Estimated Time | Type |
|-----------|----------------|------|
| 50 XP | 30 min | Pull Request |

**Prerequisite:** [Task 2.3: Clean the Data](../task-2.3/INSTRUCTIONS.md)

## Quick Links

- Your repository on GitHub
- Team Chat - Get help from mentors
- [All Tasks Overview](../../docs/)


## Objective

Create a code review checklist specifically for data cleaning pipelines, based on your experience with Tasks 2.1-2.3.

## The Situation

> **Priya (Data Lead):** "You've built a solid data cleaning pipeline. Now I want you to document what makes good data cleaning code. Create a review checklist that we can use when reviewing each other's data pipelines. Think about all the things that could go wrong and how to catch them in review."

## Why This Matters

In real data teams, code review is essential:
- Catches bugs before they hit production
- Shares knowledge across the team
- Maintains code quality standards
- Helps juniors learn from seniors

A good checklist makes reviews faster and more consistent.

## Requirements

Create a comprehensive code review checklist covering:

1. **Correctness** - Does the code actually clean the data properly?
2. **Robustness** - Does it handle edge cases and errors?
3. **Readability** - Can other team members understand it?
4. **Performance** - Is it efficient enough for production data?
5. **Testing** - How do we know it works?

## Deliverable

Create a file at:
```
code_review_checklist.md
```

## Template

```markdown
# Data Cleaning Pipeline - Code Review Checklist

## Overview
[Brief intro - when to use this checklist, what it covers]

## 1. Data Correctness

### Input Validation
- [ ] [Specific check]
- [ ] [Specific check]

### Transformation Logic
- [ ] [Specific check]
- [ ] [Specific check]

### Output Validation
- [ ] [Specific check]

## 2. Error Handling

- [ ] [Check for how errors are handled]
- [ ] [Check for edge cases]

## 3. Code Quality

### Readability
- [ ] [Specific check]
- [ ] [Specific check]

### Documentation
- [ ] [Specific check]

## 4. Performance

- [ ] [Check for efficiency issues]
- [ ] [Check for memory issues]

## 5. Testing

- [ ] [What tests should exist]
- [ ] [What test cases to verify]

## Common Issues to Watch For

[List 3-5 common mistakes you've seen or made, with examples]

### Issue 1: [Name]
**Problem:** [Description]
**What to look for:** [How to spot it in review]
**Fix:** [How to correct it]

## Quick Reference

| Category | Key Question |
|----------|-------------|
| Correctness | Does it actually fix the data issues? |
| Robustness | What happens with empty/null/weird data? |
| Readability | Could a new team member understand this? |
| Performance | Will this work on 1M rows? |
| Testing | How do we know it works? |
```

## What to Include

Base your checklist on real issues:

- Problems you encountered in Task 2.1 (data profiling)
- Validation rules from Task 2.2 (Pandera schema)
- Edge cases from Task 2.3 (cleaning pipeline)

**Example items:**
- "Does the cleaning function return a new DataFrame or modify in place?"
- "Are null values handled before operations that would fail on nulls?"
- "Is there a check for duplicate records after cleaning?"
- "Does the code log how many rows were affected by each cleaning step?"

## Evaluation

Your PR will be checked for:

- [ ] File exists at the correct path
- [ ] Checklist has at least 15 specific, actionable items
- [ ] Covers all 5 required categories
- [ ] Includes at least 3 "common issues" with examples
- [ ] Items are specific to data cleaning (not generic code review)


## How to Submit

1. **Create a branch:**
   ```bash
   git checkout -b task-2.4
   ```

2. **Do your work** in the repository root

3. **Test locally:**
   ```bash
   pytest tests/test_2_4.py -v
   ```

4. **Commit and push:**
   ```bash
   git add .
   git commit -m "Complete task 2.4"
   git push -u origin task-2.4
   ```

5. **Open a Pull Request** on GitHub and wait for CI to pass

## Tips

- Think about bugs you made (or almost made) in your cleaning code
- Good checklist items are specific and actionable
- Include code examples where helpful
- A reviewer should be able to use this without prior context

## Submission

1. Create a new branch: `git checkout -b task-2.4`
2. Create your code review checklist
3. Commit and push
4. Open a Pull Request on GitHub
5. Wait for the automated checks to pass


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
**Previous Task:** [Task 2.3: Clean the Data](../task-2.3/INSTRUCTIONS.md) | **Next Task:** [Task 3.1: Revenue Investigation](../../week-3/task-3.1/INSTRUCTIONS.md)
