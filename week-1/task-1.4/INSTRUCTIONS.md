# Task 1.4: Document the Fix

| XP Reward | Estimated Time | Type |
|-----------|----------------|------|
| 25 XP | 20 min | Pull Request |

**Prerequisite:** [Task 1.3: Fix the Date Bug](../task-1.3/INSTRUCTIONS.md)

## Quick Links

- [GitHub Repository](https://github.com/cartly-data/{your-cohort-repo})
- [Discord #ask-priya](https://discord.com/channels/cartly/ask-priya) - Get help
- [All Tasks Overview](../../docs/)


## Objective

Add troubleshooting documentation for the date parsing bug you fixed in Task 1.3, helping future team members avoid similar issues.

## The Situation

> **Priya (Data Lead):** "Nice work fixing that date bug! Now I need you to document what you found. We've had similar issues before, and good documentation helps the whole team learn. Add a troubleshooting guide to our docs."

## Requirements

Create a troubleshooting document that explains:

1. **The Problem**: What was the symptom? What error did users see?
2. **The Root Cause**: Why did this bug happen?
3. **The Solution**: How did you fix it?
4. **Prevention**: How can we avoid this in the future?

## Deliverable

Create a file at:
```
cohort/{your-github-username}/week-1/troubleshooting_date_bug.md
```

## Template

Use this structure for your document:

```markdown
# Troubleshooting: Date Parsing Bug in Data Loader

## Problem

[Describe what users experienced - e.g., "Orders showed incorrect dates" or "Data loader crashed with error X"]

## Symptoms

- [List observable symptoms]
- [Error messages if any]
- [Which data was affected]

## Root Cause

[Explain WHY the bug occurred. Be technical but clear.]

## Solution

[Describe the fix you implemented. Include code snippets if helpful.]

```python
# Example of the fix
```

## How to Prevent

[What practices would prevent this bug in the future?]

- [Tip 1]
- [Tip 2]

## Related Links

- [Link to the PR that fixed it]
- [Any relevant documentation]
```

## Evaluation

Your PR will be checked for:

- [ ] File exists at the correct path
- [ ] Document follows the template structure
- [ ] All sections are filled in with relevant content
- [ ] Explanation is clear enough for a new team member to understand


## How to Submit

1. **Create a branch:**
   ```bash
   git checkout -b task-1.4-{your-github-username}
   ```

2. **Do your work** in `cohort/{your-github-username}/`

3. **Test locally:**
   ```bash
   pytest tests/test_1_4.py -v
   ```

4. **Commit and push:**
   ```bash
   git add .
   git commit -m "Complete task 1.4"
   git push -u origin task-1.4-{your-github-username}
   ```

5. **Open a Pull Request** on GitHub and wait for CI to pass

## Tips

- Write as if explaining to someone who just joined the team
- Include the actual error message you saw (if any)
- Code examples make documentation much more useful
- Link to your Task 1.3 PR so readers can see the actual fix

## Submission

1. Create a new branch: `git checkout -b task-1.4-{your-github-username}`
2. Create your troubleshooting document
3. Commit and push: `git add . && git commit -m "Add date bug troubleshooting docs" && git push -u origin task-1.4-{your-github-username}`
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

**Still stuck?** Ask in `#ask-priya` on Discord!

---
**Previous Task:** [Task 1.3: Fix the Date Bug](../task-1.3/INSTRUCTIONS.md) | **Next Task:** [Task 2.1: Profile the Marketing Data](../../week-2/task-2.1/INSTRUCTIONS.md)
