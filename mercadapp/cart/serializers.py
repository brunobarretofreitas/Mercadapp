from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Cart, CartItem

class CartSerializer(serializers.ModelSerializer):
	cart_items = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	
	class Meta:
		model = Cart
		fields = '__all__'
		extra_kwargs = {'user': {'read_only': True}}
		
class CartItemSerializer(serializers.ModelSerializer):
	cart = serializers.PrimaryKeyRelatedField(read_only=True)
	class Meta:
		model = CartItem
		fields = '__all__'