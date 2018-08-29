from rest_framework import serializers
from apps.app import models


class CategorySerializer(serializers.ModelSerializer):
    products = serializers.ReadOnlyField(source='products_count')

    class Meta:
        model = models.Category
        fields = (
            'id',
            'name',
            'products'
        )


class ProductSerializer(serializers.ModelSerializer):
    end_price = serializers.ReadOnlyField(source='get_price')
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = models.Product
        fields = (
            'id',
            'name',
            'category',
            'category_name',
            'price',
            'end_price',
            'stock',
            'link_cover',
            'active'
        )


class SaleProductSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')
    price_item = serializers.ReadOnlyField(source='price_product')
    total_item = serializers.ReadOnlyField(source='total')

    class Meta:
        model = models.SaleProduct
        fields = (
            'id',
            'sale',
            'product',
            'product_name',
            'quantity',
            'price_item',
            'total_item'
        )


class SaleSerializer(serializers.ModelSerializer):
    total = serializers.ReadOnlyField(source='total_sale')
    products = SaleProductSerializer(many=True, read_only=True)
    products_count = serializers.ReadOnlyField(source='items')
    date = serializers.ReadOnlyField(source='get_date')

    class Meta:
        model = models.Sale
        fields = (
            'id',
            'created',
            'date',
            'user',
            'total',
            'products_count',
            'products'
        )

