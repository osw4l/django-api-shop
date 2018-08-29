from django.conf.urls import url, include
from rest_framework import routers
from .app import viewsets


router = routers.DefaultRouter()
router.register(r'categories', viewsets.CategoryViewSet)
router.register(r'products', viewsets.ProductViewSet)
router.register(r'sales', viewsets.SaleViewSet)


urlpatterns = [
    url(r'^shop/', include(router.urls))
]

