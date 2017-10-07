from rest_framework import serializers
from .models import Order, OrderInfo, Payment
from cart.models import Cart
from market.serializers import StoreSerializer

class OrderInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = OrderInfo
		exclude = ['order']

class LoggedUserCarts(serializers.PrimaryKeyRelatedField):
	def get_queryset(self):
		user = self.context['request'].user
		queryset = Cart.objects.all().filter(user=user)
		return queryset


class OrderSerializer(serializers.ModelSerializer):
	order_info = OrderInfoSerializer(read_only=True)
	cart = LoggedUserCarts()

	class Meta:
		model = Order
		fields = ['id','cart', 'order_info', 'status', 'value']
		extra_kwargs = {'value': {'read_only': True}}

class OrderDetailSerializer(serializers.ModelSerializer):
	order_info = OrderInfoSerializer(read_only=True)

	class Meta:
		model = Order
		fields = ['id','order_info', 'status', 'cart']
		extra_kwargs = {'cart': {'read_only': True}}

class PaymentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Payment
		fields = '__all__'

