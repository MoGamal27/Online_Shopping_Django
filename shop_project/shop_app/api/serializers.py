from rest_framework import serializers
from shop_app.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
        
class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.name")
    class Meta:
        model = Product
        fields = '__all__'        