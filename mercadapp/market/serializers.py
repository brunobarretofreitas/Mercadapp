from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Store, Product, Order

class StoreSerializer(serializers.ModelSerializer):
	class Meta:
		model = Store
		fields = ['id', 'name', 'zip_code']

class StoreInformationsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Store
		depth = 1
		fields = [
			'id',
			'name',
			'description',
			'store_admin',
			'zip_code',
			'telephones',
			'email',
			'logo',
			'minimum_order',
			'delivery_tax',
			'delivery_radius',]
