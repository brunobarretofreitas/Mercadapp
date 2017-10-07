from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Store, Product, Order, OrderInfo, Cart, CartItem, Payment, Delivery, DeliveryDay, DeliveryHour

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user



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


class ProductSerializer(serializers.ModelSerializer):

	class Meta:
		model = Product
		extra_kwargs = {'store': {'read_only': True}}
		fields = '__all__'

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

class PaymentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Payment
		fields = '__all__'

class DeliverySerializer(serializers.ModelSerializer):
	delivery_days = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	class Meta:
		model = Delivery
		fields = '__all__'

class DeliveryDaySerializer(serializers.ModelSerializer):
	delivery_hour = serializers.PrimaryKeyRelatedField(read_only=True)

	class Meta:
		model = DeliveryDay
		fields = '__all__'

class DeliveryHourSerializer(serializers.ModelSerializer):
	class Meta:
		model = DeliveryHour
		fields = ['initial_hour', 'end_hour',]

class OrderSerializer(serializers.ModelSerializer):
	order_info = serializers.PrimaryKeyRelatedField(read_only=True)
	class Meta:
		model = Order
		fields = '__all__'
		depth = 1

class OrderInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = OrderInfo
		fields = '__all__'