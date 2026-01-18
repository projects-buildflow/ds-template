# Task 1.1: Environment Setup

| XP Reward | Estimated Time | Type |
|-----------|----------------|------|
| 25 XP | 20 min | Token verification |

## Quick Links

- [GitHub Repository](https://github.com/cartly-data/{your-cohort-repo})
- [Discord #ask-priya](https://discord.com/channels/cartly/ask-priya) - Get help
- [All Tasks Overview](../../docs/)


## Objective

Set up your local development environment and verify everything works correctly.

## The Situation

> **Priya (Data Lead):** "Welcome to Cartly! Before you can start working on real tasks, we need to make sure your development environment is properly set up. Run through these steps and verify everything works."

## Steps

### 1. Clone the repository

If you haven't already:

```bash
git clone <your-repo-url>
cd <repo-name>
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:
- **Mac/Linux:** `source venv/bin/activate`
- **Windows:** `venv\Scripts\activate`

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Git

Make sure Git knows who you are:

```bash
git config user.name "Your Name"
git config user.email "your@email.com"
```

### 5. Verify your setup

Run the verification script:

```bash
python scripts/verify_setup.py
```

If everything is configured correctly, you'll see a verification token like:

```
CARTLY-XXXXXXXXXXXX-XXXX
```

## Submitting Your Token

You can submit your token in two ways:

### Option 1: Discord (Recommended)

In any channel, use the slash command:
```
/submit CARTLY-YOUR-TOKEN-HERE
```

### Option 2: Web Portal

Go to your Tasks page, click on Task 1.1, and enter your token in the form.

## Troubleshooting

**"Python version too low"**
- Install Python 3.8 or higher from python.org

**"Package not installed"**
- Make sure your virtual environment is activated
- Run `pip install -r requirements.txt`

**"Git not configured"**
- Run the git config commands in step 4

**Script not found**
- Make sure you're in the repository root directory
- The script is at `scripts/verify_setup.py`

## Tips

- Keep your virtual environment activated while working on tasks
- If you have multiple Python versions, use `python3` instead of `python`
- Ask in `#ask-priya` if you get stuck!

---

**Next Task:** [Task 1.2: Join the Team](../task-1.2/INSTRUCTIONS.md)
