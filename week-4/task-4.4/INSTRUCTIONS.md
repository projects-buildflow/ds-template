# Task 4.4: Final Presentation

| XP Reward | Estimated Time | Type |
|-----------|----------------|------|
| 150 XP | 120 min | AI presentation review |

**Prerequisite:** [Task 4.3: Debug AI Code](../task-4.3/INSTRUCTIONS.md)

## Quick Links

- [GitHub Repository](https://github.com/cartly-data/{your-cohort-repo})
- [Discord #ask-priya](https://discord.com/channels/cartly/ask-priya) - Get help
- [All Tasks Overview](../../docs/)


## Objective

Present your internship journey to the team.

## The Situation

It's your last day! Priya has asked you to present your work to the team. This is your chance to showcase what you've learned and accomplished.

## Steps

1. **Create your presentation**

   Save as: `cohort/{your-github-username}/week-4/presentation.pdf`

2. **Include these sections:**

   | Section | Slides | Content |
   |---------|--------|---------|
   | Introduction | 1 | Who you are, your background |
   | Journey | 1-2 | Your path through the internship |
   | Key Project | 2-3 | Deep dive into your best work |
   | Learnings | 1 | What you learned, challenges overcome |
   | Future | 1 | What you want to learn next |

3. **Requirements:**
   - 6-10 slides total
   - Include at least one data visualization
   - Keep text minimal - use bullet points
   - Include speaker notes or a separate script (optional)

## Presentation Tips

### Lead with Impact
- "I built X which does Y" is better than "I worked on X"
- Quantify when possible: "Reduced processing time by 50%"

### Show, Don't Tell
- Include screenshots of your work
- Add code snippets that you're proud of
- Show before/after comparisons

### Be Specific
- "Fixed 3 data validation bugs" > "Improved data quality"
- "Built pipeline processing 10K records daily" > "Built data pipeline"

### Keep It Visual
- One idea per slide
- Large fonts (24pt minimum)
- Images and charts over walls of text

## Example First Slide

```
MY DATA INTERNSHIP JOURNEY
━━━━━━━━━━━━━━━━━━━━━━━━━━

{your-name}
Data Analytics Intern

━━━━━━━━━━━━━━━━━━━━━━━━━━

Week 1: Environment setup & first bug fix
Week 2: Built data validation system
Week 3: Investigated revenue drop → found root cause
Week 4: Automated daily analytics pipeline

Key Achievement: Reduced manual reporting time by 80%
```

## Example Key Project Slide

```
REVENUE INVESTIGATION
━━━━━━━━━━━━━━━━━━━━━

The Challenge:
• Revenue down 15%
• CEO needed answers before board meeting

My Analysis:
• [Chart showing revenue trend]
• Identified root cause: shipping delays

Impact:
• Presented findings to leadership
• Recommendations implemented within 1 week
```

## Test Locally

```bash
pytest tests/test_4_4.py -v --student-folder=cohort/{your-github-username}
```

## Creating Your PDF

- Google Slides: File → Download → PDF
- PowerPoint: File → Export → PDF
- Keynote: File → Export To → PDF
- Canva: Download → PDF

## Evaluation

Your presentation will be reviewed by AI for:
- All required sections present
- Clear and professional design
- Includes data visualization
- Appropriate length (6-10 slides)

## Congratulations!

If you've made it here, you've completed the Cartly Data Internship. You should be proud of what you've accomplished!

What you've learned:
- Setting up professional development environments
- Writing production-quality data cleaning code
- Building data validation systems
- Conducting business analysis
- Optimizing SQL queries
- Creating dashboards
- Designing and building data pipelines
- Debugging code and documenting your work
- Presenting technical work professionally

Good luck with your data career!


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
**Previous Task:** [Task 4.3: Debug AI Code](../task-4.3/INSTRUCTIONS.md)
