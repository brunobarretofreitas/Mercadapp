# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics

from .models import *
from .views import *
from .serializers import *
from market.models import Store
from mercadapp.permissions import IsStoreAdmin

# Create your views here.
class PaymentList(generics.ListCreateAPIView):
	queryset = Payment.objects.all()
	serializer_class = PaymentSerializer

class OrderList(generics.ListAPIView):
	serializer_class = OrderSerializer
	permission_classes = (IsStoreAdmin,)

	def get_queryset(self):
		user = self.request.user
		store = Store.objects.get(store_admin=user)
		return Order.objects.all().filter(store=store)


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Order.objects.all()
	serializer_class = OrderDetailSerializer

class OrderInfo(generics.ListCreateAPIView):
	queryset = OrderInfo.objects.all()
	serializer_class = OrderInfoSerializer

	def perform_create(self, serializer):
		order = Order.objects.get(pk=self.kwargs['pk'])
		serializer.save(order=order)

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
