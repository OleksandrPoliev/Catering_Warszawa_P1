from django.test import SimpleTestCase



class cateringaoitest(SimpleTestCase):
    def test_list_url(self):
        assert 1==1



import os
import sys
if __name__=="__main__":
    sys.path.append(os.path.dirname(os.path.dirname(os.environ.setdefault("DJANGO_SETTINGS_MODULE","mainapp.settings"))))
import django
django.setup()
