"""
tasks/urls.py — App-Level URL Configuration
=============================================
This file defines URL patterns for the 'tasks' app specifically.
The project-level urls.py (taskmanager/urls.py) delegates to this file
using include('tasks.urls').

HOW URL PATTERNS WORK:
  path('<pattern>', <view>, name='<name>')

  - pattern: The URL to match. Can be:
      - Empty string '': matches the root (e.g., /tasks/ if included with tasks/)
      - Plain string: 'create/' matches /tasks/create/
      - Converter: '<int:pk>/' matches /tasks/42/ and passes pk=42 to the view
      - '<int:pk>/update/': matches /tasks/42/update/

  - view: The view to call (either a function or ClassName.as_view())
    - FBVs are referenced directly: task_create_view
    - CBVs use .as_view(): TaskListView.as_view()

  - name: A unique name for this URL (used in templates and reverse())
    - In templates: {% url 'tasks:task_list' %}
    - In Python: reverse('tasks:task_list')
    - The 'tasks:' prefix comes from the app_name below

URL CONVERTERS:
  <int:pk>   → matches an integer, passes it as pk=42 to the view
  <str:slug> → matches text with hyphens
  <slug:slug>→ matches only slug-safe characters
"""

from django.urls import path
from . import views  # Import views from THIS app (the dot means "current package")

# app_name sets the URL namespace for this app.
# This means URL names are prefixed with 'tasks:' to avoid naming conflicts
# between apps. For example: 'tasks:task_list' instead of just 'task_list'.
# In templates, you use: {% url 'tasks:task_list' %}
app_name = 'tasks'

urlpatterns = [
    # --- List View ---
    # URL: /tasks/
    # Matches the empty string (because the project urls.py already matched 'tasks/')
    # View: TaskListView (CBV) — shows all tasks
    # Name: 'task_list' (namespaced: 'tasks:task_list')
    path('', views.TaskListView.as_view(), name='task_list'),

    # --- Detail View ---
    # URL: /tasks/42/
    # <int:pk> is a URL CONVERTER: it matches an integer and passes it
    # to the view as a keyword argument named 'pk' (primary key).
    # Django uses pk to look up the specific Task from the database.
    path('<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),

    # --- Create View ---
    # URL: /tasks/create/
    # Uses our FBV (Function-Based View) — notice no .as_view() needed!
    path('create/', views.task_create_view, name='task_create'),

    # --- Update View ---
    # URL: /tasks/42/update/
    # Combines the pk converter with a literal path segment 'update/'
    path('<int:pk>/update/', views.TaskUpdateView.as_view(), name='task_update'),

    # --- Delete View ---
    # URL: /tasks/42/delete/
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
]
