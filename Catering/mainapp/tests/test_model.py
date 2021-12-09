from django.test import SimpleTestCase


class Testurls(SimpleTestCase):
    def test_list_url(self):
        assert 1 == 1




from django.test import TestCase

from django.core.files.uploadedfile import SimpleUploadedFile

from decimal import Decimal


from Catering.mainapp.models import Categori,Product,Customer,Contact,Order,OrderItem
class CateringtestCases(TestCase):
    def setUp(self) :
        self.user=Customer.object.create(username="testuser",password='password')
        self.category=Categori.objects.create(type='rybne',slug ='rybne')
        self.t=Categori.objects.create(type='rybne',slug ='rybne')
        image=SimpleUploadedFile("ord.jpg",content=b"",content_type="image/jpg")
        self.product=Product.objects.create(
            category=self.category,
            title='testprod',
            slug='testslug',
            image=image,
            components='blabla',
            price=Decimal("50"),
            allergy="testalergi"
                )
        self.customer=Customer.objects.create(username=self.user,email="emailtest@gmail.com",password1="blablaZ1",password2="blabalZ1",imie="imez",nazwisko='testnaz',adres='aleje jez')
        self.contect=Contact.objects.create(email="emailtest@gmail.com", temat = 'models.CharField(max_length=255)',wiadomosc=' models.TextField()')
        self.order=Order.objects.create(address = 'models.CharField(max_length=250)', kod_pocztowy =' models.xh=20)',)
        self.orderItem=OrderItem.objects.create( order=self.order ,product=self.product,price=Decimal('20'),Ilość=2)


    def test_categori(self):
        self.assertIn(self.category,self.t)

    def test_add_to_orderItem(self):
        self.orderItem.product.add(self.product)
        self.assertIn(self.orderItem,self.product.all())
        self.assertEqual(self.orderItem.count(),1 )
        self.assertEqual(self.orderItem.price,Decimal(20))



    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)

class CateringtestCases(TestCase):
    t=1
    d=1
    def test_a(self):
        t = 1
        d = 1
        self.assertIn(t,d)
        self.assertEqual(t,d )
