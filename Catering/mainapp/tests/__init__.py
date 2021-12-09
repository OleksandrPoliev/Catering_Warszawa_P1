import sys
import django
import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'Catering.settings'
django.setup()
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()