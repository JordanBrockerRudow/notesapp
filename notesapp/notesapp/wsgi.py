"""
WSGI config for notesapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
from secret import SECRET_KEY

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notesapp.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Prod')
os.environ.setdefault('DJANGO_SECRET_KEY', SECRET_KEY)

from configurations.wsgi import get_wsgi_application

application = get_wsgi_application()
