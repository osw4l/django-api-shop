from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from apps.app import models
from . import serializers
from .utils import LoginPermission


class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

    @detail_route(methods=['GET'])
    def products(self, request, pk=None):
        products = models.Product.objects.filter(category_id=pk)
        serializer = serializers.ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductViewSet(ReadOnlyModelViewSet):
    queryset = models.Product.objects.filter(active=True)
    serializer_class = serializers.ProductSerializer


class SaleViewSet(ModelViewSet):
    queryset = models.Sale.objects.all()
    serializer_class = serializers.SaleSerializer
    permission_classes = (LoginPermission,)

    def get_queryset(self):
        return models.Sale.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        shop = models.Sale.objects.create(user=self.request.user)
        print(data)
        for item in data:
            if item is not None:
                print(item)
                shop.add_item(
                    id_product=item['id'],
                    quantity=item['items']
                )

        return Response({
            'success': True
        })
