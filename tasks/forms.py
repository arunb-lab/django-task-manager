"""
tasks/forms.py — Django Forms
==============================
A FORM in Django handles:
  1. Rendering HTML form fields (text inputs, checkboxes, etc.)
  2. Validating submitted data (checking required fields, max lengths, etc.)
  3. Saving valid data to the database

MODELFORM vs FORM:
  - django.forms.Form: A generic form. You define every field manually.
  - django.forms.ModelForm: A form LINKED to a model. Django automatically
    generates the form fields from your model fields. Much less code!

We use ModelForm here because:
  - It mirrors our Task model automatically
  - It handles saving to the database with form.save()
  - It knows validation rules from the model (e.g., max_length=200)
"""

from django import forms
from .models import Task  # Import the model we want to create a form for


class TaskForm(forms.ModelForm):
    """
    TaskForm is a ModelForm for creating and editing Task records.

    The inner 'Meta' class tells Django:
      - WHICH model this form is for (model = Task)
      - WHICH fields to include (fields = [...])
      - Optionally: how to render each field (widgets = {...})
    """

    class Meta:
        # model: Which model should this form create/edit?
        model = Task

        # fields: Which fields from the model to include in the form.
        # We exclude 'created_at' and 'updated_at' because those are
        # auto-set by Django — the user shouldn't fill them in.
        fields = ['title', 'description', 'is_complete']

        # widgets: Customize how each field is rendered as HTML.
        # By default, Django renders fields with basic HTML inputs.
        # Here we customize the CSS classes for Bootstrap-friendly styling.
        widgets = {
            # TextInput for the title field (single-line text)
            'title': forms.TextInput(attrs={
                'class': 'form-input',            # CSS class for styling
                'placeholder': 'Enter task title...',  # Hint text in the input
            }),

            # Textarea for the description field (multi-line text)
            'description': forms.Textarea(attrs={
                'class': 'form-textarea',
                'rows': 4,                         # How many rows tall
                'placeholder': 'Optional: Add more details...',
            }),

            # CheckboxInput for the boolean is_complete field
            'is_complete': forms.CheckboxInput(attrs={
                'class': 'form-checkbox',
            }),
        }

    def clean_title(self):
        """
        CUSTOM VALIDATION for the 'title' field.

        Django calls clean_<fieldname>() methods automatically during form
        validation. This is where you add field-specific validation logic.

        Rules:
          - Django first runs built-in validation (required, max_length, etc.)
          - Then it calls your clean_title() method
          - If you raise forms.ValidationError, the error shows in the form
          - Otherwise, return the (possibly cleaned) value
        """
        title = self.cleaned_data.get('title', '')

        # Example custom rule: title can't be just whitespace
        if not title.strip():
            raise forms.ValidationError("Title cannot be blank or just spaces.")

        # Return the cleaned value (we strip whitespace from both ends)
        return title.strip()
