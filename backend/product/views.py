from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from product.models import Product, Category
from product.serializers import ProductSerializer, CategorySerializer


# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = (IsAuthenticated,)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = (IsAuthenticated,)
