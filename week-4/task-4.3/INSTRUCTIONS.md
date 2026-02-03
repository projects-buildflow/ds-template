# Task 4.3: Debug AI Code

| XP Reward | Estimated Time | Type |
|-----------|----------------|------|
| 75 XP | 45 min | PR with automated tests |

**Prerequisite:** [Task 4.2: Implement Pipeline](../task-4.2/INSTRUCTIONS.md)

## Quick Links

- Your repository on GitHub
- Team Chat - Get help from mentors
- [All Tasks Overview](../../docs/)


## Objective

Find and fix bugs in AI-generated code.

## The Situation

A junior developer used AI to generate a data validator, but it has bugs. Your job: find the bugs, fix them, and document what you found.

## Steps

1. **Review the buggy code**

   Look at `week-4/task-4.3/ai_generated_validator.py`

2. **Create your fixed version**

   Create: `fixed_validator.py`

3. **Document the bugs**

   Create: `bug_report.md`

## The Challenge

The validator has **exactly 5 bugs**. Can you find them all?

## Bug Report Format

```markdown
# Bug Report: AI-Generated Validator

## Bug 1: [Short description]
**Location**: Line XX
**Problem**: What was wrong
**Impact**: What could go wrong because of this bug
**Fix**: How you fixed it

## Bug 2: [Short description]
...
```

## Hints

- Test with edge cases (empty strings, boundary values)
- Look carefully at comparison operators
- Check regex patterns
- Consider logical operators (and/or)
- Think about what "valid" really means for each field

## Example Bug Report Entry

```markdown
## Bug 1: Off-by-one error in age validation
**Location**: Line 45, `_validate_age` method
**Problem**: Uses `> 120` instead of `>= 120`
**Impact**: Allows age 120 which should be considered invalid (unrealistic age)
**Fix**: Changed comparison to `>= 120`
```

## Test Cases to Try

```python
# These test cases may reveal bugs!
test_cases = [
    # Valid data - should pass
    {"name": "John", "email": "john@test.com", "age": 25, "phone": "1234567890"},

    # Edge cases - check carefully
    {"name": "Test", "email": "test@test.com", "age": 120, "phone": "1234567890"},
    {"name": "Test", "email": "test@test.com", "age": 25, "phone": ""},
    {"name": "Test", "email": "test@testXcom", "age": 25, "phone": "1234567890"},
]
```

## Test Locally

```bash
pytest tests/test_4_3.py -v
```


## How to Submit

1. **Create a branch:**
   ```bash
   git checkout -b task-4.3
   ```

2. **Do your work** in the repository root

3. **Test locally:**
   ```bash
   pytest tests/test_4_3.py -v
   ```

4. **Commit and push:**
   ```bash
   git add .
   git commit -m "Complete task 4.3"
   git push -u origin task-4.3
   ```

5. **Open a Pull Request** on GitHub and wait for CI to pass

## Tips

- Run the original code with test cases to see the bugs in action
- Think like a tester - what inputs would break this?
- AI-generated code often has subtle logic errors
- The bugs are real programming mistakes, not tricks

## Evaluation

Automated tests will run your fixed validator against edge cases. Your bug report will be reviewed for completeness.


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
**Previous Task:** [Task 4.2: Implement Pipeline](../task-4.2/INSTRUCTIONS.md) | **Next Task:** [Task 4.4: Final Presentation](../task-4.4/INSTRUCTIONS.md)
