"""
taskmanager/wsgi.py — WSGI Configuration
==========================================
WSGI stands for "Web Server Gateway Interface". It's the standard interface
between Python web applications and web servers (like Gunicorn, uWSGI, Apache).

For BEGINNERS: You don't need to touch this file during development.
Django's built-in development server (python manage.py runserver) doesn't
even use this file — it uses its own server.

This file becomes important when you deploy to production (e.g., on Heroku,
DigitalOcean, AWS, etc.). The production web server uses this file to talk
to your Django application.
"""

import os
from django.core.wsgi import get_wsgi_application

# Tell Django which settings file to use
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskmanager.settings')

# This is the WSGI application object. Production servers use this.
application = get_wsgi_application()
