# Contributing to Django Task Manager

> **Welcome from anywhere in the world! 🌍**  
> This project exists to teach Django to beginners globally. Every contribution — code, docs, translations, or bug reports — makes it better for thousands of learners. **No contribution is too small.**

---

## Table of Contents

- [Who Can Contribute?](#who-can-contribute)
- [Ways to Contribute](#ways-to-contribute)
- [Your First Contribution (Step by Step)](#your-first-contribution-step-by-step)
- [Development Setup](#development-setup)
- [Branch Naming & Commit Style](#branch-naming--commit-style)
- [Running Tests](#running-tests)
- [Code Style Guidelines](#code-style-guidelines)
- [Submitting a Pull Request](#submitting-a-pull-request)
- [What Happens After You Submit?](#what-happens-after-you-submit)
- [Ideas for Contributions](#ideas-for-contributions)
- [Code of Conduct](#code-of-conduct)

---

## Who Can Contribute?

**Everyone.** Seriously.

- 👨‍💻 **Beginners** learning Django for the first time
- 🌎 **International developers** — English is not required (open an issue in your language!)
- 🏫 **Teachers** who want to improve the explanations
- 🔬 **Experienced developers** who want to add advanced sections
- 🎨 **Designers** who want to improve the UI
- 📝 **Writers** who want to fix typos or improve documentation

---

## Ways to Contribute

| Type | Examples | Skill Level |
|------|----------|-------------|
| 🐛 Report a bug | Found something broken | Any |
| 📄 Improve docs | Fix typos, add examples | Any |
| ❓ Ask a question | Open a Discussion | Any |
| 🏫 Improve explanations | Make comments clearer | Beginner |
| ✅ Write tests | Add unit tests | Beginner/Intermediate |
| ✨ Add a feature | See Ideas section below | Intermediate |
| 🌐 Translations | README in other languages | Any |
| 🔧 Fix a bug | See open issues | Intermediate |
| 📈 Improve CI/CD | Better pipeline | Advanced |

---

## Your First Contribution (Step by Step)

Never contributed to open source before? Perfect — this project is beginner-friendly by design.

### Step 1: Fork the Repository

Click the **Fork** button at the top right of the repository page. This creates your own copy of the project on GitHub.

### Step 2: Clone Your Fork

```bash
git clone https://github.com/YOUR-USERNAME/django-task-manager.git
cd django-task-manager
```

### Step 3: Set Up the Upstream Remote

This connects your local copy to the original repository so you can pull in updates.

```bash
git remote add upstream https://github.com/arunb-lab/django-task-manager.git
git remote -v  # Verify: you should see both 'origin' and 'upstream'
```

### Step 4: Create a Branch

Never work directly on `main`. Create a new branch for each feature or fix.

```bash
# Pull the latest changes first
git checkout main
git pull upstream main

# Create your branch (see naming conventions below)
git checkout -b feature/add-task-priority
```

### Step 5: Make Your Changes

Write your code, add tests, update documentation as needed.

### Step 6: Run Tests Locally

```bash
# Make sure all tests pass before committing
python manage.py test tasks --verbosity=2
```

### Step 7: Commit Your Changes

```bash
git add .
git commit -m "feat: add priority field to Task model"
```

### Step 8: Push to Your Fork

```bash
git push origin feature/add-task-priority
```

### Step 9: Open a Pull Request

Go to your fork on GitHub and click **"Compare & pull request"**.
Fill in the PR template and submit. That's it!

---

## Development Setup

```bash
# 1. Clone and enter the project
git clone https://github.com/YOUR-USERNAME/django-task-manager.git
cd django-task-manager

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Mac/Linux
# venv\Scripts\activate         # Windows

# 3. Install dependencies
pip install -r requirements.txt
pip install flake8 coverage     # Dev tools

# 4. Apply migrations
python manage.py migrate

# 5. Create a superuser (for admin panel testing)
python manage.py createsuperuser

# 6. Run the server
python manage.py runserver
# Visit: http://127.0.0.1:8000/tasks/
```

---

## Branch Naming & Commit Style

### Branch Names

```
feature/short-description     # New features
fix/short-description         # Bug fixes
docs/short-description        # Documentation only
test/short-description        # Tests only
refactor/short-description    # Code cleanup
```

**Examples:**
```
feature/add-task-priority
fix/form-validation-error
docs/improve-readme-setup
test/add-task-model-tests
```

### Commit Messages

Use the conventional commits format:

```
type: short description (max 72 chars)

Optional longer explanation here.
```

**Types:** `feat`, `fix`, `docs`, `test`, `refactor`, `style`, `chore`

**Good examples:**
```
feat: add due date field to Task model
fix: task form not saving description when empty
docs: add setup instructions for Windows users
test: add unit tests for TaskForm validation
```

---

## Running Tests

```bash
# Run all tests
python manage.py test

# Run tests with output
python manage.py test tasks --verbosity=2

# Run with coverage report
coverage run --source=. manage.py test tasks
coverage report
coverage html  # Opens htmlcov/index.html in browser
```

The CI pipeline runs these automatically on every push and PR.

---

## Code Style Guidelines

- Follow **PEP 8** (Python style guide)
- Max line length: **120 characters**
- Use **4 spaces** for indentation (no tabs)
- Add **docstrings** to all functions and classes
- Comment the **why**, not just the what (this is a teaching project!)
- Keep functions short and single-purpose

Run the linter before committing:

```bash
flake8 . --exclude=migrations --max-line-length=120
```

---

## Submitting a Pull Request

1. Make sure the CI pipeline is **green** (✅)
2. Fill in the **PR template** completely
3. Link the issue your PR resolves (`Closes #42`)
4. Keep PRs **focused** — one feature/fix per PR
5. Be patient and responsive to feedback

---

## What Happens After You Submit?

1. The CI pipeline runs automatically (tests, linting, security checks)
2. A maintainer reviews your code and may request changes
3. Once approved, your PR is merged into `main`
4. **Your name appears in the contributor list!** 🎉

---

## Ideas for Contributions

Looking for something to work on? Here are ideas by difficulty:

### 🟢 Beginner (Great First Issues)
- Add more comments/explanations to any existing file
- Fix typos in README or code comments
- Add a `verbose_name` to all model fields
- Add a test for the task list page
- Translate README to another language

### 🟡 Intermediate
- Add a `priority` field (Low / Medium / High) to the Task model
- Add due date support (`DateField`) with overdue detection
- Add a search bar to filter tasks by title
- Add pagination to the task list (Django's `Paginator`)
- Write a full test suite (aim for 80%+ coverage)
- Add a `category` or `tag` field to tasks

### 🔴 Advanced
- Add user authentication (each user sees only their tasks)
- Add a REST API using Django REST Framework
- Deploy to Railway or Render with a production `settings_prod.py`
- Add real-time updates with Django Channels / WebSockets
- Add a Docker + docker-compose setup
- Add internationalization (i18n) support

---

## Code of Conduct

We are building a **global, inclusive community** for Django learners.

- **Be kind and respectful** — everyone was a beginner once
- **Welcome newcomers** — especially those from non-English backgrounds
- **Give constructive feedback** — explain the why, not just the what
- **Celebrate contributions** — no PR is too small
- **Zero tolerance** for harassment, discrimination, or negativity

By contributing, you agree to uphold these values.

---

## Thank You! 💖

Every issue, PR, and comment helps make Django more accessible to learners worldwide.  
You are part of something global. Let's build together!

**Star the repo ⭐ and share it to help more beginners find it.**

[![GitHub stars](https://img.shields.io/github/stars/arunb-lab/django-task-manager?style=social)](https://github.com/arunb-lab/django-task-manager)
