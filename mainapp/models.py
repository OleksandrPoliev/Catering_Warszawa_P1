from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.text import slugify





class CategoriManager(models.Manager):

    def getQueryset(self):
        return super().get_queryset()

class Categori(models.Model):
    type = models.CharField(max_length=200, verbose_name="imie kategori")
    slug = models.SlugField(unique=True)
    titletext = models.TextField(verbose_name="składniki",default="some inf")
    objects = CategoriManager()

    def __str__(self):
        return self.type

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.type)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('mainapp:Categori', kwargs={'the_slug': self.slug})



class Product(models.Model):
    category = models.ForeignKey(Categori, verbose_name="kategoria", on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name="zdjęcie")
    components = models.TextField(verbose_name="składniki")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="cena")
    allergy = models.TextField(verbose_name="alergia")
    objects = models.Manager()

    class Meta:
        index_together = (('id', "slug"),)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(self, 'mainapp/Product_data.html', kwargs={'pcslug': self.slug})


class Customer(AbstractUser):
    telefon = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    adres = models.CharField(max_length=120)

    def __str__(self):
        return self.email



class Contact(models.Model):
    email = models.EmailField()
    temat = models.CharField(max_length=255)
    wiadomosc = models.TextField()

    def __str__(self):
        return self.email




class Order(models.Model):

    address = models.CharField(max_length=250)
    kod_pocztowy = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    Ilość = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.Ilość


