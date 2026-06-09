"""
taskmanager/urls.py — Project-Level URL Configuration
======================================================
This is the ROOT URL configuration for the entire Django project.
Think of it as the "main switchboard" for all incoming web requests.

HOW URL ROUTING WORKS:
1. A browser sends a request to your server (e.g., GET /tasks/)
2. Django loads THIS file (specified in settings.py ROOT_URLCONF)
3. Django tries to match the URL path against each pattern in urlpatterns
4. When a match is found, Django hands off to the matched view or app urls.py

KEY CONCEPT — include():
  Instead of listing every single URL in this file, we use include() to
  delegate to the app's own urls.py. This keeps things organized:
  - Project urls.py handles top-level routing
  - App urls.py handles app-specific routing
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # --- Django Admin ---
    # The built-in admin panel is available at /admin/
    # Django generates this entire interface automatically from your models!
    path('admin/', admin.site.urls),

    # --- Tasks App URLs ---
    # Any URL starting with 'tasks/' is handed off to tasks/urls.py
    # include('tasks.urls') means: "go look in the tasks app's urls.py file"
    #
    # Example: A request for /tasks/1/ will:
    #   1. Match 'tasks/' here
    #   2. Pass '1/' to tasks/urls.py for further matching
    path('tasks/', include('tasks.urls')),
]
