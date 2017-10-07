# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework import status
from rest_framework import generics

from django.shortcuts import render
from .serializers import StoreSerializer, OrderInfoSerializer, ProductSerializer, UserSerializer, CartSerializer, CartItemSerializer, OrderSerializer, PaymentSerializer, DeliverySerializer, DeliveryDaySerializer, DeliveryHourSerializer
from .models import Store, Product, Order, OrderInfo, Cart, Payment, CartItem, Delivery, DeliveryDay, DeliveryHour

# Create your views here.
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)

    def perform_create(self, serializer):
    	serializer.save(store_admin=self.request.user)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)


class StoreList(generics.ListCreateAPIView):
	serializer_class = StoreSerializer
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		stores = Store.objects.all()
		for store in stores:
			if store.can_deliver("61601310") is False:
				stores = Store.objects.exclude(id=store.id)

		return stores

	def perform_create(self, serializer):
		serializer.save(store_admin=self.request.user)

class StoresDeliverable(generics.ListCreateAPIView):
	serializer_class = StoreSerializer
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		stores = Store.objects.all()
		for store in stores:
			if store.can_deliver(self.kwargs['location']) is False:
				stores = Store.objects.exclude(id=store.id)

		return stores

	def perform_create(self, serializer):
		serializer.save(store_admin=self.request.user)

class StoreDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Store.objects.all()
	serializer_class = StoreSerializer

class ProductList(generics.ListCreateAPIView):
	serializer_class = ProductSerializer

	def get_queryset(self):
		store = Store.objects.get(pk=self.kwargs['pk'])
		products = Product.objects.all().filter(store=store)
		return products

	def perform_create(self, serializer):
		user = self.request.user
		store = user.store
		serializer.save(store=store)

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

class UserCarts(generics.ListCreateAPIView):
	serializer_class = CartSerializer

	def get_queryset(self):
		user = self.request.user
		return Cart.objects.filter(user=user)

	def perform_create(self, serializer):
		user = self.request.user
		serializer.save(user=user)

class CartDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Cart.objects.all()
	serializer_class = CartSerializer

class PaymentList(generics.ListCreateAPIView):
	queryset = Payment.objects.all()
	serializer_class = PaymentSerializer

class CartItems(generics.ListCreateAPIView):
	serializer_class = CartItemSerializer

	def get_queryset(self):
		cart = Cart.objects.get(pk=self.kwargs['pk'])
		return CartItem.objects.all().filter(cart=cart)

	def perform_create(self, serializer):
		cart = Cart.objects.get(pk=self.kwargs['pk'])
		serializer.save(cart=cart)

class CartItemDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = CartItem.objects.all()
	serializer_class = CartItemSerializer

class StoreDeliveryList(generics.ListCreateAPIView):
	serializer_class = DeliverySerializer

	def get_queryset(self):
		store = Store.objects.get(pk=self.kwargs['pk'])
		return Delivery.objects.all().filter(store=store)

	def perform_create(self, serializer):
		store = Store.objects.get(pk=self.kwargs['pk'])
		serializer.save(store=store)

class StoreDeliveryDay(generics.ListCreateAPIView):
	serializer_class = DeliveryDaySerializer

	def get_queryset(self):
		store = Store.objects.get(pk=self.kwargs['pk'])
		delivery_days = DeliveryDay.objects.all().filter(delivery=store.delivery)
		return delivery_days

	def perform_create(self, serializer):
		store = Store.objects.get(pk=self.kwargs['pk'])
		serializer.save(delivery=store.delivery)

class StoreDeliveryHour(generics.CreateAPIView):
	serializer_class = DeliveryHourSerializer

	def perform_create(self, serializer):
		delivery_day = DeliveryDay.objects.get(pk=self.kwargs['pk'])
		serializer.save(delivery_day=delivery_day)

class OrderList(generics.ListCreateAPIView):
	serializer_class = OrderSerializer

	def get_queryset(self):
		user = self.request.user
		return Order.objects.all()

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer


class OrderInfo(generics.ListCreateAPIView):
	queryset = OrderInfo.objects.all()
	serializer_class = OrderInfoSerializer

class OrderStatusNew(generics.ListAPIView):
	queryset = Order.objects.all().filter(status='N')
	serializer_class = OrderSerializer

class OrderStatusApproved(generics.ListAPIView):
	queryset = Order.objects.all().filter(status='A')
	serializer_class = OrderSerializer

class OrderStatusSent(generics.ListAPIView):
	queryset = Order.objects.all().filter(status='S')
	serializer_class = OrderSerializer

class OrderStatusDelivered(generics.ListAPIView):
	queryset = Order.objects.all().filter(status='D')
	serializer_class = OrderSerializer
