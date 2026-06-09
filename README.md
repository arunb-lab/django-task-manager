# Django Task Manager — Beginner's Learning Project

A complete, beginner-friendly Django project that teaches core Django concepts through a real working **Task Manager** application. Every file is heavily commented to explain *why*, not just *what*.

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

---

## Project Structure

```
django-task-manager/          ← Root folder (your working directory)
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
│   ├── __init__.py
│   ├── admin.py              ← Register models for the admin panel
│   ├── apps.py               ← App configuration
│   ├── forms.py              ← ModelForm for creating/editing tasks
│   ├── models.py             ← The Task model (maps to a database table)
│   ├── urls.py               ← URL patterns for the tasks app
│   └── views.py              ← Views: both FBV and CBV examples
│
├── manage.py                 ← Django's command-line utility
├── requirements.txt          ← Python dependencies
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

A virtual environment keeps this project's dependencies isolated from other projects.

```bash
# Create the virtual environment
python -m venv venv

# Activate it (Mac/Linux)
source venv/bin/activate

# Activate it (Windows)
venv\Scripts\activate

# Your prompt should now show (venv)
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run Migrations

Migrations create the database tables based on the models defined in `models.py`.

```bash
python manage.py migrate
```

You should see output like:
```
Applying tasks.0001_initial... OK
```

### 6. Create a Superuser (for Django Admin)

```bash
python manage.py createsuperuser
# Enter a username, email, and password when prompted
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

## Learning Exercises

Once the app is running, try these to deepen your understanding:

1. **Add a new field** to the `Task` model (e.g., `priority`). Run `makemigrations` and `migrate`.
2. **Create a new view** that shows only completed tasks.
3. **Add a search bar** to the task list that filters by title.
4. **Style the app** by adding Bootstrap CSS to `base.html`.
5. **Add user authentication** so each user can only see their own tasks.

---

## License

MIT — free to use for learning.
