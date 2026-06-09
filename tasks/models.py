"""
tasks/models.py — Database Models
====================================
A MODEL is a Python class that represents a DATABASE TABLE.
Each attribute on the class represents a COLUMN in that table.
Each instance of the class represents a ROW (a single record).

When you define a model, Django can:
  1. Create the database table for you (via migrations)
  2. Give you a Python API to create, read, update, and delete records
     (the Django ORM — Object Relational Mapper)

WHAT IS AN ORM?
  Instead of writing raw SQL like:
    SELECT * FROM tasks_task WHERE is_complete = 1;

  You write Python like:
    Task.objects.filter(is_complete=True)

  Django translates your Python into SQL automatically. This means you
  don't need to know SQL to use Django (though it helps!).
"""

from django.db import models
from django.urls import reverse


class Task(models.Model):
    """
    The Task model — represents a single task in our task manager.

    Django will create a database table called 'tasks_task' for this model.
    (The naming pattern is: <app_name>_<model_name_lowercase>)

    Django also AUTOMATICALLY adds an 'id' field (integer primary key)
    to every model. You don't need to define it yourself.
    """

    # --- CharField: for short text (with a maximum length) ---
    # This becomes a VARCHAR column in the database.
    # max_length=200 means the title can be at most 200 characters.
    title = models.CharField(
        max_length=200,
        help_text="Enter a short title for the task (max 200 characters)"
    )

    # --- TextField: for longer, open-ended text (no max length) ---
    # This becomes a TEXT column in the database.
    # blank=True means the field is OPTIONAL in forms (can be submitted empty).
    # null=True means the database column can store NULL (no value at all).
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Optional: Add more details about the task"
    )

    # --- BooleanField: stores True or False ---
    # default=False means new tasks start as "not complete".
    is_complete = models.BooleanField(
        default=False,
        help_text="Check this box when the task is done"
    )

    # --- DateTimeField with auto_now_add=True ---
    # auto_now_add=True: automatically sets this field to NOW when a
    # new Task is created. You never set this manually.
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Automatically set to the date/time the task was created"
    )

    # --- DateTimeField with auto_now=True ---
    # auto_now=True: automatically updates this field to NOW every time
    # the Task is saved (useful for tracking last modifications).
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Automatically updated every time the task is saved"
    )

    # --- Meta class: model-level configuration ---
    class Meta:
        # ordering tells Django how to sort Tasks by default.
        # '-created_at' means: newest tasks first (the '-' means descending).
        ordering = ['-created_at']

        # verbose_name is used in the admin panel (singular form)
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        """
        __str__ is a special Python method that returns a human-readable
        string representation of the object.

        Django uses this in the admin panel, in debug output, and whenever
        you print or display a Task object.

        Without this method, Django would show something like <Task: Task object (1)>.
        With this method, it shows the actual task title.
        """
        return self.title

    def get_absolute_url(self):
        """
        get_absolute_url is a Django convention: it returns the URL for
        viewing this specific object.

        reverse('tasks:task_detail', kwargs={'pk': self.pk}) generates the URL
        for this task's detail page. We use reverse() instead of hardcoding
        the URL so that if we ever change our URL patterns, this still works.

        'tasks:task_detail' means: look in the 'tasks' app namespace for
        a URL named 'task_detail'.
        """
        return reverse('tasks:task_detail', kwargs={'pk': self.pk})
