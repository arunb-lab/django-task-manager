# Django Task Manager — Beginner's Learning Project

[![Django CI](https://github.com/arunb-lab/django-task-manager/actions/workflows/ci.yml/badge.svg)](https://github.com/arunb-lab/django-task-manager/actions/workflows/ci.yml)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![Django 4.2](https://img.shields.io/badge/django-4.2-green.svg)](https://www.djangoproject.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Contributors](https://img.shields.io/github/contributors/arunb-lab/django-task-manager)](https://github.com/arunb-lab/django-task-manager/graphs/contributors)

> 🌍 **This project is open to contributors worldwide!**  
> A complete, beginner-friendly Django project that teaches core Django concepts through a real working **Task Manager** application. Every file is heavily commented to explain *why*, not just *what*.

---

## What You Will Learn

By studying and running this project, you will understand:

- The difference between a Django **project** and an **app**
- How **models** define your database schema
- What **migrations** are and why they matter
- How to write **Function-Based Views (FBVs)** and **Class-Based Views (CBVs)**
- How **URL routing** works at the project and app level
- How to use **template inheritance** (a base layout + child pages)
- How to build **forms** with `ModelForm`
- How to perform full **CRUD** (Create, Read, Update, Delete)
- How to use the **Django Admin** panel
- How **CI/CD pipelines** work with GitHub Actions

---

## Project Structure

```
django-task-manager/          ← Root folder (your working directory)
│
├── .github/                   ← GitHub-specific files
│   ├── workflows/
│   │   └── ci.yml            ← GitHub Actions CI/CD pipeline
│   ├── ISSUE_TEMPLATE/       ← Bug report & feature request forms
│   └── pull_request_template.md
│
├── taskmanager/              ← Django PROJECT folder (created with startproject)
│   ├── __init__.py           ← Makes this a Python package
│   ├── settings.py           ← All project settings (database, apps, etc.)
│   ├── urls.py               ← Root URL configuration
│   └── wsgi.py               ← Entry point for web servers
│
├── tasks/                    ← Django APP folder (created with startapp)
│   ├── migrations/           ← Database migration files (auto-generated)
│   │   └── 0001_initial.py
│   ├── templates/            ← HTML templates for this app
│   │   └── tasks/
│   │       ├── base.html     ← Base template (shared layout)
│   │       ├── task_list.html
│   │       ├── task_detail.html
│   │       ├── task_form.html
│   │       └── task_confirm_delete.html
│   ├── admin.py              ← Register models for the admin panel
│   ├── apps.py               ← App configuration
│   ├── forms.py              ← ModelForm for creating/editing tasks
│   ├── models.py             ← The Task model (maps to a database table)
│   ├── urls.py               ← URL patterns for the tasks app
│   └── views.py              ← Views: both FBV and CBV examples
│
├── manage.py                 ← Django's command-line utility
├── requirements.txt          ← Python dependencies
├── CONTRIBUTING.md           ← How to contribute to this project
├── .gitignore                ← Files Git should not track
└── README.md                 ← This file
```

---

## How Django Works (Overview for Beginners)

When a user visits a URL in your app, Django follows this flow:

```
Browser Request
      ↓
  urls.py (project)      ← Decides which app handles the URL
      ↓
  urls.py (app)          ← More specific URL matching
      ↓
  views.py               ← Business logic: fetch data, process forms
      ↓
  models.py              ← Talks to the database (via ORM)
      ↓
  templates/*.html       ← Renders HTML with the data
      ↓
Browser Response
```

### Key Concepts

**Project vs App**
A Django *project* is the entire website configuration. An *app* is a self-contained module within the project. One project can have many apps (e.g., tasks, users, blog).

**Models & Migrations**
A model is a Python class that represents a database table. When you change a model, you run `makemigrations` to create a migration file, then `migrate` to apply it to the database. Think of migrations as a version history for your database.

**Views**
Views are Python functions (or classes) that receive a web request and return a response. A Function-Based View (FBV) is a plain function. A Class-Based View (CBV) inherits from Django's built-in generic views and reduces boilerplate.

**Templates**
Templates are HTML files with special Django tags like `{{ variable }}` and `{% tag %}`. Template inheritance lets you define a base layout once and extend it in child templates.

**URLs**
The `urls.py` files map URL patterns to views. The project `urls.py` delegates to app-level `urls.py` files using `include()`.

**Django ORM**
The Object-Relational Mapper lets you interact with the database using Python instead of SQL. For example: `Task.objects.all()` instead of `SELECT * FROM tasks_task;`

---

## Setup Instructions (Step by Step)

### 1. Prerequisites

Make sure you have Python 3.8+ installed:

```bash
python --version
# Should show Python 3.8 or higher
```

### 2. Clone the Repository

```bash
git clone https://github.com/arunb-lab/django-task-manager.git
cd django-task-manager
```

### 3. Create and Activate a Virtual Environment

```bash
# Create the virtual environment
python -m venv venv

# Activate it (Mac/Linux)
source venv/bin/activate

# Activate it (Windows)
venv\\Scripts\\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Create a Superuser (for Django Admin)

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:
- **App**: http://127.0.0.1:8000/tasks/
- **Admin**: http://127.0.0.1:8000/admin/

---

## Features

| Feature | View Type | URL |
|---------|-----------|-----|
| List all tasks | Class-Based View (ListView) | `/tasks/` |
| View task details | Class-Based View (DetailView) | `/tasks/<id>/` |
| Create a new task | Function-Based View | `/tasks/create/` |
| Edit a task | Class-Based View (UpdateView) | `/tasks/<id>/update/` |
| Delete a task | Class-Based View (DeleteView) | `/tasks/<id>/delete/` |

---

## CI/CD Pipeline

This project uses **GitHub Actions** for Continuous Integration. Every push and Pull Request automatically:

1. ✅ Runs the test suite on **Python 3.9, 3.10, and 3.11**
2. 💎 Lints the code with **flake8**
3. ⚙️ Runs **Django system checks** (`manage.py check`)
4. 🔒 Audits dependencies for **security vulnerabilities**
5. 📈 Generates a **coverage report**

Check the **Actions tab** to see pipeline runs: [GitHub Actions](https://github.com/arunb-lab/django-task-manager/actions)

---

## Contributing — Help This Go Global! 🌍

**We want this to be the #1 Django learning resource for beginners worldwide.**

Whether you're a first-time open source contributor or an experienced developer, **your contribution matters**. Here's how you can help:

- 🐛 **Found a bug?** [Open a bug report](https://github.com/arunb-lab/django-task-manager/issues/new?template=bug_report.md)
- ✨ **Have an idea?** [Request a feature](https://github.com/arunb-lab/django-task-manager/issues/new?template=feature_request.md)
- 📚 **Improve docs** — fix typos, add examples, translate to another language
- ✅ **Write tests** — help us reach 100% coverage
- 🌐 **Translate** — make this accessible in your language
- 🏫 **Add features** — see the ideas list in [CONTRIBUTING.md](CONTRIBUTING.md)

**Read [CONTRIBUTING.md](CONTRIBUTING.md) for the full step-by-step guide.**

> 👋 **New to open source?** This project has "good first issue" labels. Every PR is welcome, no matter how small. We were all beginners once.

---

## Learning Exercises

Once the app is running, try these to deepen your understanding:

1. **Add a new field** to the `Task` model (e.g., `priority`). Run `makemigrations` and `migrate`.
2. **Create a new view** that shows only completed tasks.
3. **Add a search bar** to the task list that filters by title.
4. **Style the app** by adding Bootstrap CSS to `base.html`.
5. **Add user authentication** so each user can only see their own tasks.
6. **Write tests** using Django's `TestCase` — run with `python manage.py test`

---

## Star & Share ⭐

If this project helped you learn Django, please:

- ⭐ **Star this repo** to help others find it
- 🔁 **Share it** with friends learning Python/Django
- 🌍 **Tell your local meetup** — help us reach learners in every country

**Together we can make quality Django education free and accessible to everyone.**

---

## License

MIT — free to use, modify, and share for learning.
