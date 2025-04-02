from django.db import transaction
from rest_framework import serializers
from .models import User, Product


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password', 'user_permissions', 'is_authenticated', 'get_full_name', 'orders')
        # exclude = ('password', 'user_permissions')
        # fields = '__all__'     

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'description',
            'name',
            'price',
            'stock',
        )

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Price must be greater than 0."
            )
        return value        