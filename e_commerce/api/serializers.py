from rest_framework import serializers
from  .models import Product,Cart,CartProduct

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = "__all__"
class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True,read_only=True)
    class Meta:
        model = Cart
        fields ="__all__"




