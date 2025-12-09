from django.urls import path
from .views import (
    CategoryListCreateView,
    CategoryRetrieveUpdateDeleteView,
    ProductListCreateView,
    ProductRetrieveUpdateDeleteView,
)

urlpatterns = [
    # Category endpoints
    path("categories/", CategoryListCreateView.as_view(), name="category-list"),
    path("categories/<int:pk>/", CategoryRetrieveUpdateDeleteView.as_view(), name="category-detail"),

    # Product endpoints
    path("products/", ProductListCreateView.as_view(), name="product-list"),
    path("products/<int:pk>/", ProductRetrieveUpdateDeleteView.as_view(), name="product-detail"),
]
