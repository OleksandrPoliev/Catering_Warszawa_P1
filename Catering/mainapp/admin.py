from django.contrib import admin

from .models import *


@admin.register(Categori)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('type',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', "slug", 'image', 'components', 'allergy', "price"]
    list_editable = ["price"]


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'address', 'kod_pocztowy', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]


admin.site.register(Customer)
admin.site.register(Contact)

admin.site.register(Order, OrderAdmin)
