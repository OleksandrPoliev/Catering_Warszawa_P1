from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .form import Registr_new_user, ContactForm, Calc, CartaddForm, OrderCreateForm
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, View
from .models import Product, Categori, OrderItem
from django.views.generic import ListView
from .cart import Cart
from django.views.decorators.http import require_POST
from django.views.generic.edit import FormMixin


class Productdetailvies(FormMixin, DetailView):
    model = Product
    template_name = "mainapp/Product_data.html"
    context_object_name = 'Product'
    form_class = CartaddForm
    slug_url_kwarg = 'pcslug'

    def get_context_data(self, **kwargs):
        context = super(Productdetailvies, self).get_context_data(**kwargs)
        context['form_class'] = self.get_form
        return context


class Startpage(View):

    def get(self, request, *args, **kwargs):
        categori = Categori.objects.all()
        products = Product.objects.all()

        context = {'categori': categori,
                   "products": products}
        return render(request, "mainapp/spage.html", context)


class Categori_detail_Viev(ListView):
    model = Product

    template_name = "mainapp/Categori.html"
    context_object_name = 'categori'

    def get_queryset(self):
        return Product.objects.all().filter(category__slug=self.kwargs["the_slug"])


    def get_context_data(self, **kwargs):
        context = super(Categori_detail_Viev, self).get_context_data(**kwargs)
        context['Cat'] = Categori.objects.filter(slug__exact=self.kwargs["the_slug"])
        return context

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartaddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, Ilość=cd['Ilość'], o_Ilość=cd['o_Ilość'])

    return redirect(('mainapp:detail'))


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect(('mainapp:detail'))


def cart_detail(request):
    cart = Cart(request)
    return render(request, "mainapp/detail.html", {"cart": cart})


@login_required
def profile(request):
    return render(request, "mainapp/konto_użytkownika.html")


def register(request):
    if request.method == "POST":
        form = Registr_new_user(request.POST)

        if form.is_valid():
            form.save()
            user = form.save()
            user.is_active = False
            email_body = "Witam z stworzeniam kanta na WarszawGO  wejść na stronę http://127.0.0.1:8000/"
            email_subject = "WarszawG0 konto"
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(email_subject, email_body, to=[to_email])

            email.send()

            messages.success(request, "Witam Rejestracja zakończona.")
            return redirect("http://127.0.0.1:8000/%5Elogin/$")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = Registr_new_user()
    return render(request, "mainapp/rejestracja.html", {"form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

            else:
                pass
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "mainapp/login.html", context={"login_form": form})


def contactV(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("http://127.0.0.1:8000/")
    form = ContactForm()
    context = {"form": form}
    return render(request, "mainapp/contact.html", context)


def calc(request):
    form = Calc(request.POST or None)
    bmr_result = 0

    if form.is_valid():
        Wiek = form.cleaned_data.get("Wiek")
        Jestes = form.cleaned_data.get("Jestes")
        Waga = form.cleaned_data.get("Waga")
        Wzrost = form.cleaned_data.get("Wzrost")
        Ile_razy_w_tygodniu_uprawiasz_60_min_sportu = form.cleaned_data.get(
            "Ile_razy_w_tygodniu_uprawiasz_60_min_sportu")
        Jaki_masz_cel = form.cleaned_data.get("Jaki_masz_cel")

        data_for_sport = {'0': 1.1, '1': 1.2, '2': 1.3, '3': 1.4, '4': 1.5,
                          '5': 1.6, '6': 1.7, '7': 1.8}
        cel = {'Chcę schudnąć': -500, 'Chcę zdrowo jeść': 0,
               'Chcę zbudować mięśnie': 500}

        if Jestes == 'Mężczyzna':
            c1 = 66
            hm = 6.2 * Wzrost
            wm = 12.7 * Waga
            am = 6.76 * Wiek
            bmr_result += c1 + hm + wm - am

        if Jestes == 'Kobieta':
            c1 = 655.1
            hm = 4.35 * Wzrost
            wm = 4.7 * Waga
            am = 4.7 * Wiek
            bmr_result += c1 + hm + wm - am

        cal_data_for_calori = cel.get(Jaki_masz_cel)
        sport_data = data_for_sport.get(Ile_razy_w_tygodniu_uprawiasz_60_min_sportu)

        bmr_result *= sport_data
        bmr_result += cal_data_for_calori

    k = int(bmr_result)

    context = {"form": form, "k": k}
    return render(request, "mainapp/calc.html", context)


def order_create(request):
    cart = Cart(request)

    if request.method == 'POST':

        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         Ilość=item['Ilość'])

            cart.clear()
            return render(request, 'mainapp/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'mainapp/create.html',
                  {'cart': cart, 'form': form})
