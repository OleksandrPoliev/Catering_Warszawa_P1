from .views import Startpage, profile, register, \
    Categori_detail_Viev, contactV, calc, Productdetailvies, cart_add, cart_detail, cart_remove, order_create
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

app_name = "mainapp"

urlpatterns = [


    path('create/', order_create, name='order_create'),
    path("", Startpage.as_view(), name="home"),
    path(r"^Kosz/$", cart_detail, name="detail"),
    path(r"^odjąć/(?P<product_id>\d+)/$", cart_remove, name="cart_remove"),
    path(r"^dodac/(?P<product_id>\d+)/$", cart_add, name="cart_add"),
    path(r'^menu/(?P<the_slug>[-a-zA-Z0-9_]+)/', Categori_detail_Viev.as_view(), name="Categori"),
    path(r"^menu/(?P<the_slug>[-a-zA-Z0-9_]+)/(?P<pcslug>[-a-zA-Z0-9_]+)$'>", Productdetailvies.as_view(),
         name="Product_data"),
    path(r"^konto_użytkownika/$", profile, name='konto_użytkownika'),
    path(r"^rejestracja/$", register, name="rejestracja"),
    path(r"^login/$", auth_views.LoginView.as_view(template_name="mainapp/login.html"), name="login"),
    path(r"^logout/$", auth_views.LogoutView.as_view(template_name="mainapp/logout.html"), name="logout"),
    path(r"^contact/$", contactV, name="contact"),
    path(r"^calculator_kalori/$", calc, name="calc"),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
