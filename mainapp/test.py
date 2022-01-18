from django.test import SimpleTestCase
from django.test import TestCase
from .models import Categori
class Testurls(SimpleTestCase):
    def test_dummy(self):
        self.assertEqual(1, 1)
    def test_list_url(self):
        assert 1 == 1

class YourTestClass(TestCase):
        def setUp(self):
            Categori.objects.create(type="rybne",slug="rybne",titletext="testinfo")



    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)

