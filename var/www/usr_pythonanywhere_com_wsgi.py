import sys
import os

path = '/home/observatory/notesapp/notesapp/'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SECRET_KEY'] = '' # TO DO: Add secret key
os.environ['DJANGO_SETTINGS_MODULE'] = 'notesapp.settings'
os.environ['DJANGO_CONFIGURATION'] = 'Prod'

from configurations.wsgi import get_wsgi_application
application = get_wsgi_application()