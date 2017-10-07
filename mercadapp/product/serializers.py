from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):

	class Meta:
		model = Product
		extra_kwargs = {'store': {'read_only': True}}
		fields = '__all__'
