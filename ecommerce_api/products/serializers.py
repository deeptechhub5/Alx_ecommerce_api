from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "description"]

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True, source='category')

    class Meta:
        model = Product
        fields = [
            "id", "name", "description", "price", "stock",
            "category", "category_id", "image_url", "created_at", "updated_at"
        ]
        read_only_fields = ["created_at", "updated_at"]
