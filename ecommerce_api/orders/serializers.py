from rest_framework import serializers
from .models import Wishlist, CartItem, Cart
from products.serializers import ProductSerializer


class WishlistSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Wishlist
        fields = ["id", "product", "added_at"]


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ["id", "product", "quantity"]


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ["id", "items", "created_at"]
