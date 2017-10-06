from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Store, Product, Order

class StoreSerializer(serializers.ModelSerializer):
	store_admin = serializers.CharField(source='store_admin.username', read_only=True)	

	class Meta:
		model = Store
		depth = 1
		fields = [
			'id',
			'name',
			'description',
			'store_admin',
			'zip_code',
			'telephone',
			'email',
			'logo',
			'minimum_order',
			'delivery_tax',
			'delivery_radius',]

class UserSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = User
		fields = ('id', 'username', 'first_name')


class ProductSerializer(serializers.ModelSerializer):

	class Meta:
		model = Product
		fields = ['id', 'name', 'value']