import sys
import django
import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'Catering.settings'
django.setup()
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from django.test import SimpleTestCase
class Testurls(SimpleTestCase):
    def test_dummy(self):
        self.assertEqual(1, 1)
    def test_list_url(self):
        assert 1 == 1


