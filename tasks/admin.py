"""
tasks/admin.py — Django Admin Configuration
=============================================
The Django Admin is a FREE, automatically-generated web interface that lets
you manage your database records without writing any extra code.

To access it:
  1. Run: python manage.py createsuperuser
  2. Start the server: python manage.py runserver
  3. Visit: http://127.0.0.1:8000/admin/

You'll be able to create, edit, and delete Task records directly from
a web interface. Django builds this entire interface from your models!

REGISTERING A MODEL:
  To make a model visible in the admin, you must REGISTER it here.
  There are two ways:
    1. Simple: admin.site.register(Task)
    2. Custom: Create a ModelAdmin class for more control (shown below)
"""

from django.contrib import admin
from .models import Task  # Import our Task model from this app


# Option 1: Simple registration (one line — admin gets basic defaults)
# admin.site.register(Task)

# Option 2: Custom ModelAdmin (more control over how it looks in admin)
@admin.register(Task)  # This decorator is equivalent to admin.site.register(Task, TaskAdmin)
class TaskAdmin(admin.ModelAdmin):
    """
    TaskAdmin customizes how the Task model appears in the Django Admin.
    You can control the list display, filters, search, and more.
    """

    # list_display: Which fields to show as COLUMNS in the list view
    # The first field ('title') also becomes a clickable link.
    list_display = ('title', 'is_complete', 'created_at', 'updated_at')

    # list_filter: Adds a sidebar with filter options.
    # Click "Yes" or "No" to filter tasks by completion status.
    list_filter = ('is_complete',)

    # search_fields: Adds a search bar at the top.
    # Admin will search in the 'title' and 'description' fields.
    search_fields = ('title', 'description')

    # list_editable: Lets you edit these fields directly in the list view
    # without clicking into each record.
    list_editable = ('is_complete',)

    # ordering: Default sort order in the admin list view.
    ordering = ('-created_at',)  # Newest first

    # readonly_fields: These fields can't be edited (they're auto-set by Django)
    readonly_fields = ('created_at', 'updated_at')
