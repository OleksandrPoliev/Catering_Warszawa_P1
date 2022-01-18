from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.forms import TextInput
from .models import Customer, Contact, Order


class Registr_new_user(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')
    telefon = forms.CharField(validators=[phone_regex], max_length=17)
    imie = forms.CharField(max_length=20)
    nazwisko = forms.CharField(max_length=20)
    adres = forms.CharField(max_length=120)

    class Meta:
        model = Customer
        fields = ["username", "email", "password1", "password2", "telefon", "imie", "nazwisko", "adres"]


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class Calc(forms.Form):
    Jestes = [('Mężczyzna', "Mężczyzna"), ('Kobieta', "Kobieta")]
    Ile_razy_w_tygodniu_uprawiasz_60_min_sportu = [('0', "0"), ('1', "1"), ('2', '2'), ('3', "3"), ('4', "4"),
                                                   ('5', '5'), ('6', "6"), ('7', '7')]
    Jaki_masz_cel = [('Chcę schudnąć', "Chcę schudnąć"), ('Chcę zdrowo jeść', "Chcę zdrowo jeść"),
                     ('Chcę zbudować mięśnie', 'Chcę zbudować mięśnie')]
    Wiek = forms.IntegerField()
    Jestes = forms.ChoiceField(choices=Jestes)
    Waga = forms.IntegerField()
    Wzrost = forms.IntegerField()
    Ile_razy_w_tygodniu_uprawiasz_60_min_sportu = forms.ChoiceField(choices=Ile_razy_w_tygodniu_uprawiasz_60_min_sportu)
    Jaki_masz_cel = forms.ChoiceField(choices=Jaki_masz_cel)


PROD_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 31)]


class CartaddForm(forms.Form):
    Ilość = forms.TypedChoiceField(choices=PROD_QUANTITY_CHOICES, coerce=int)
    o_Ilość = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [ 'address', 'kod_pocztowy', ]
        widgets = {
            'user': TextInput(attrs={'readonly': 'readonly'})
        }



