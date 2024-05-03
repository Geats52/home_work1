from django.contrib import admin

from .models import Client, Product, Order
from decimal import Decimal

DISCOUNT = 10


@admin.action(description="apply  discount")
def apply_discount(modeladmin, request, queryset):
    for product in queryset:
        product.price -= (product.price * Decimal(DISCOUNT / 100))
        product.save()
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'photo']
    ordering = ['-quantity']
    list_filter = ['added_date', 'price', 'quantity']
    search_fields = ['description', 'name']
    search_help_text = 'Поиск по названию или описанию продукта/товара'
    actions = [apply_discount]
    readonly_fields = ['added_date']
    fieldsets = [
        ('Общие данные', 
         {
             'classes': ['wide'], 
             'fields': ['name', 'price', 'quantity']
             }
        ),
        (
            'Описание', 
            {
                'classes': ['collapse'], 
                'fields': ['description', 'photo']
                }
        ),
        (
            'Дата добавления', 
            {
                'fields': ['added_date']
                }
        ),
    ]



class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    search_fields = ['name', 'email', 'phone_number', 'address']
    search_help_text = 'name, email, phone_number, address'
    readonly_fields = ['registration_date']
    fieldsets = [
        ('Общие данные', 
         {
             'classes': ['wide'], 
             'fields': ['name', 'email', 'phone_number', 'address']
             }
        ),
        (
            None, 
            {'fields': ['registration_date']
             }
        )
    ]



class OrderAdmin(admin.ModelAdmin):
    @staticmethod
    def get_client_name(obj):
        return obj.client.name

    list_display = ['get_client_name', 'total_amount', 'order_date']
    ordering = ['-order_date', '-total_amount', ]
    search_fields = ['client_name', 'total_amount']
    search_help_text = 'Поиск заказов клиента по имени или по общей сумме заказа'
    readonly_fields = ['client', 'total_amount', 'products', 'order_date']
    list_filter = ['client', 'total_amount']
    fieldsets = [
        ('Общие данные',
         {
             'classes': ['wide'], 
             'fields': ['client', 'total_amount', 'order_date']
             }
        ),
        (
            'Заказные товары', 
            {'classes': ['collapse'], 
             'fields': ['products']
             }
        )
    ]



admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OrderAdmin)
