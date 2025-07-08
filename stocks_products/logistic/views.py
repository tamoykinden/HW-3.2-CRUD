from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # Добавляем поиск по названию и описанию
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']
    # Добавляем пагинацию
    pagination_class = LimitOffsetPagination


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # Добавляем фильтрацию по продукту и поиск
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['positions__product']  # Фильтр по ID продукта
    search_fields = ['positions__product__title', 'positions__product__description']  # Поиск по названию/описанию продукта
    # Добавляем пагинацию
    pagination_class = LimitOffsetPagination
