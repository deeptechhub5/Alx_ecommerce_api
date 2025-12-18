from django.urls import path
from .views import (
    WishlistListCreateView,
    WishlistDeleteView,
    CartView,
    AddToCartView,
    RemoveFromCartView,
)

urlpatterns = [
    # Wishlist
    path("wishlist/", WishlistListCreateView.as_view()),
    path("wishlist/<int:product_id>/", WishlistDeleteView.as_view()),

    # Cart
    path("cart/", CartView.as_view()),
    path("cart/add/", AddToCartView.as_view()),
    path("cart/remove/<int:product_id>/", RemoveFromCartView.as_view()),
]
