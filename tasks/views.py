"""
tasks/views.py — Views (Controllers)
======================================
A VIEW is a Python function (or class) that:
  1. Receives a web request
  2. Does some work (queries the database, processes a form, etc.)
  3. Returns a web response (usually rendered HTML)

Think of views as the "controllers" in MVC architecture.

There are two styles of views in Django:

FUNCTION-BASED VIEWS (FBV):
  - Simple Python functions
  - Easy to understand for beginners
  - Full control over every line of code
  - Great for: simple pages, custom logic, learning

CLASS-BASED VIEWS (CBV):
  - Python classes that inherit from Django's generic view classes
  - Much less boilerplate code
  - Built-in handling for common patterns (list, detail, create, update, delete)
  - Great for: standard CRUD operations, when you want DRY code

In this file, we use BOTH so you can compare them:
  - task_create_view: FBV (so you can see exactly what happens)
  - TaskListView: CBV (ListView — shows a list of objects)
  - TaskDetailView: CBV (DetailView — shows one object)
  - TaskUpdateView: CBV (UpdateView — edit form for one object)
  - TaskDeleteView: CBV (DeleteView — confirm & delete one object)
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.contrib import messages

from .models import Task
from .forms import TaskForm


# =============================================================================
# FUNCTION-BASED VIEW (FBV) — Create Task
# =============================================================================
def task_create_view(request):
    """
    task_create_view handles the "create a new task" page.

    This is a FUNCTION-BASED VIEW — just a plain Python function.
    It handles two scenarios based on the HTTP method:

    GET request (user visits the page):
      - Create an empty form
      - Render the template with the blank form

    POST request (user submits the form):
      - Create a form with the submitted data
      - Validate the data
        - If VALID: save to database, redirect to task list
        - If INVALID: re-render the form with error messages shown

    This pattern (GET shows form, POST processes form) is the standard
    Django form handling pattern. You'll use it constantly.
    """

    # Check the HTTP method: GET means "show me the form",
    # POST means "here is my filled-in form data"
    if request.method == 'POST':
        # request.POST is a dictionary-like object of submitted form data
        # We pass it to TaskForm so it can validate and process the data
        form = TaskForm(request.POST)

        if form.is_valid():
            # form.is_valid() runs all validation rules.
            # If all checks pass, cleaned data is in form.cleaned_data.

            # form.save() creates a new Task object in the database.
            # It returns the newly created Task instance.
            task = form.save()

            # messages.success() adds a one-time "flash message" that will
            # be displayed in the template on the next page load.
            messages.success(request, f'Task "{task.title}" created successfully!')

            # redirect() sends the user to a different URL.
            # 'tasks:task_list' is the URL name defined in tasks/urls.py.
            return redirect('tasks:task_list')

        # If form is NOT valid, we fall through to re-render with errors.
        # The form object contains error messages that the template displays.

    else:
        # GET request: create an empty form
        form = TaskForm()

    # render() combines a template with a context dictionary and returns HTML.
    # 'tasks/task_form.html' is the template file to use.
    # context is a dictionary passed to the template as variables.
    return render(request, 'tasks/task_form.html', {
        'form': form,
        'page_title': 'Create New Task',  # Used by the template
        'button_label': 'Create Task',
    })


# =============================================================================
# CLASS-BASED VIEWS (CBV)
# =============================================================================

class TaskListView(ListView):
    """
    TaskListView displays a list of all tasks.

    This is a CLASS-BASED VIEW using Django's built-in ListView.
    ListView automatically:
      1. Queries the database: Task.objects.all() (using the model attribute)
      2. Passes the results to the template as 'object_list' (or the
         custom context_object_name we set below)
      3. Renders the template

    Compare to what you'd write as an FBV:
      def task_list_view(request):
          tasks = Task.objects.all()
          return render(request, 'tasks/task_list.html', {'task_list': tasks})

    ListView does all of that in just a few class attributes!
    """

    model = Task  # Which model to list

    # template_name: Which template to render.
    # Default would be 'tasks/task_list.html' anyway (app_name/model_list.html)
    # but we specify it explicitly for clarity.
    template_name = 'tasks/task_list.html'

    # context_object_name: What variable name to use in the template.
    # Default is 'object_list', but 'task_list' is more descriptive.
    context_object_name = 'task_list'

    def get_queryset(self):
        """
        Override get_queryset to customize which objects are returned.

        The default would be Task.objects.all(). Here we add ordering
        to make sure completed tasks appear at the bottom.
        """
        # Order by: incomplete tasks first (is_complete=False sorts before True)
        # Then within each group, newest first (-created_at)
        return Task.objects.order_by('is_complete', '-created_at')


class TaskDetailView(DetailView):
    """
    TaskDetailView displays the details of a single task.

    DetailView automatically:
      1. Gets the task by primary key (from the URL parameter 'pk')
      2. Returns 404 if the task doesn't exist
      3. Passes the task to the template as 'object' (or context_object_name)
    """

    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'  # Use 'task' instead of 'object' in template


class TaskUpdateView(UpdateView):
    """
    TaskUpdateView handles editing an existing task.

    UpdateView automatically:
      1. Fetches the task by pk from the URL
      2. GET request: Pre-fills the form with current data, renders template
      3. POST request: Validates and saves changes to the database
      4. On success: Redirects to success_url
    """

    model = Task
    form_class = TaskForm  # Use our custom form (with widgets and validation)
    template_name = 'tasks/task_form.html'

    # success_url: Where to redirect after a successful update.
    # reverse_lazy() is like reverse(), but deferred — it doesn't evaluate
    # the URL until it's actually needed. Required in class bodies because
    # URL patterns aren't loaded yet when the class is defined.
    success_url = reverse_lazy('tasks:task_list')

    def get_context_data(self, **kwargs):
        """
        get_context_data lets us add extra variables to the template context.
        We use it here to customize the page title and button label.
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = f'Edit Task: {self.object.title}'
        context['button_label'] = 'Save Changes'
        return context

    def form_valid(self, form):
        """
        form_valid() is called when the submitted form passes validation.
        We override it to add a success message.
        """
        response = super().form_valid(form)
        messages.success(self.request, f'Task "{self.object.title}" updated successfully!')
        return response


class TaskDeleteView(DeleteView):
    """
    TaskDeleteView handles deleting a task.

    DeleteView automatically:
      1. GET request: Shows a confirmation page (are you sure?)
      2. POST request: Deletes the object and redirects to success_url

    This two-step process (confirm then delete) is important for safety —
    you don't want users accidentally deleting things.
    """

    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('tasks:task_list')

    def form_valid(self, form):
        """Add a success message before the object is deleted."""
        task_title = self.object.title  # Capture title before deletion
        response = super().form_valid(form)
        messages.success(self.request, f'Task "{task_title}" deleted.')
        return response
