from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Store, Delivery, DeliveryDay, DeliveryHour

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
			'minimum_order',
			'delivery_tax',
			'delivery_radius',]

class DeliveryHourSerializer(serializers.ModelSerializer):
	class Meta:
		model = DeliveryHour
		fields = ['initial_hour', 'end_hour',]

class DeliveryDaySerializer(serializers.ModelSerializer):
	delivery_hour = DeliveryHourSerializer(read_only=True)

	class Meta:
		model = DeliveryDay
		depth = 1
		fields = ('id', 'week_day', 'delivery_hour')


class DeliverySerializer(serializers.ModelSerializer):
	delivery_days = DeliveryDaySerializer(many=True, read_only=True)
	
	class Meta:
		model = Delivery
		fields = ('id', 'delivery_days', 'store')
