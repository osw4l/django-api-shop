from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'category',
                    'get_price',
                    'stock',
                    'link_cover',
                    'active'
                    ]

    actions = ['enable', 'disable']

    def enable(self, request, queryset):
        queryset.update(active=True)

    def disable(self, request, queryset):
        queryset.update(active=False)

    enable.short_description = 'enable'
    disable.short_description = 'disable'


@admin.register(models.Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'created',
        'user',
        'total_sale'
    ]


@admin.register(models.SaleProduct)
class SaleProductAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'sale',
        'product',
        'price_product',
        'quantity',
        'total'
    ]


