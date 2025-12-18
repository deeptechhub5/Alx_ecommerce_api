from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


# CATEGORY CRUD 

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CategoryRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# PRODUCT CRUD + SEARCH + FILTERING + PAGINATION 

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by("-created_at")
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]

    # Filtering
    filterset_fields = {
        "category": ["exact"],
        "price": ["gte", "lte"],
        "stock": ["gte", "lte"]
    }

    # Searching
    search_fields = ["name", "description"]

    # Ordering
    ordering_fields = ["price", "created_at", "stock"]


class ProductRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
