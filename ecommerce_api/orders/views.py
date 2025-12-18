from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Wishlist, Cart, CartItem
from .serializers import WishlistSerializer, CartSerializer
from products.models import Product


#WISHLIST 

class WishlistListCreateView(generics.ListCreateAPIView):
    serializer_class = WishlistSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        product_id = request.data.get("product_id")
        product = Product.objects.get(id=product_id)
        Wishlist.objects.get_or_create(user=request.user, product=product)
        return Response({"message": "Added to wishlist"}, status=201)


class WishlistDeleteView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, product_id):
        Wishlist.objects.filter(user=request.user, product_id=product_id).delete()
        return Response({"message": "Removed from wishlist"})


 #CART 

class CartView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        return cart


class AddToCartView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        product_id = request.data.get("product_id")
        quantity = int(request.data.get("quantity", 1))
        cart, _ = Cart.objects.get_or_create(user=request.user)
        product = Product.objects.get(id=product_id)

        item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            item.quantity += quantity
        item.save()

        return Response({"message": "Product added to cart"}, status=201)


class RemoveFromCartView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, product_id):
        cart = Cart.objects.get(user=request.user)
        CartItem.objects.filter(cart=cart, product_id=product_id).delete()
        return Response({"message": "Removed from cart"})
