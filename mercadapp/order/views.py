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
	"""
    List and Create Mercadapp's available Payment methods
    """
	queryset = Payment.objects.all()
	serializer_class = PaymentSerializer

class OrderList(generics.ListAPIView):
	"""
    List all the Store's orders of the logged Store Admin
    """
	serializer_class = OrderSerializer
	permission_classes = (IsStoreAdmin,)

	def get_queryset(self):
		user = self.request.user
		store = Store.objects.get(store_admin=user)
		return Order.objects.all().filter(store=store)


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
    Retrive, Update and Delete an Order
    """
	queryset = Order.objects.all()
	serializer_class = OrderDetailSerializer

class OrderInfo(generics.ListCreateAPIView):
	"""
    List and Create Info about an Order
    """
	queryset = OrderInfo.objects.all()
	serializer_class = OrderInfoSerializer

	def perform_create(self, serializer):
		order = Order.objects.get(pk=self.kwargs['pk'])
		serializer.save(order=order)

class OrderStatusNew(generics.ListAPIView):
	"""
    List all the orders with NEW status
    """
	queryset = Order.objects.all().filter(status='N')
	serializer_class = OrderSerializer

class OrderStatusApproved(generics.ListAPIView):
	"""
    List all the orders with APPROVED status
    """

	queryset = Order.objects.all().filter(status='A')
	serializer_class = OrderSerializer

class OrderStatusSent(generics.ListAPIView):
	"""
    List all the orders with SENT status
    """
	queryset = Order.objects.all().filter(status='S')
	serializer_class = OrderSerializer

class OrderStatusDelivered(generics.ListAPIView):
	"""
    List all the orders with DELIVERED status
    """
	queryset = Order.objects.all().filter(status='D')
	serializer_class = OrderSerializer
