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
from .serializers import *
from .models import *
from product.serializers import ProductSerializer
# Create your views here.

class StoreList(generics.ListCreateAPIView):
	"""
	get:
    List all the Stores available
    
    post:
    Creates a new Store (Only Store Admin PERMISSION)
    """
	queryset = Store.objects.all()
	serializer_class = StoreSerializer
	permission_classes = (IsAuthenticated,)


	def perform_create(self, serializer):
		serializer.save(store_admin=self.request.user)

class StoresDeliverable(generics.ListAPIView):
	"""
    List all the Stores available to deliver based on user location(CEP: XXXXXXXX)
    """

	serializer_class = StoreSerializer

	def get_queryset(self):
		stores = Store.objects.all()
		for store in stores:
			if store.can_deliver(self.kwargs['location']) is False:
				stores = Store.objects.exclude(id=store.id)

		return stores

class StoreDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
    Store Details
    """

	queryset = Store.objects.all()
	serializer_class = StoreSerializer

class StoreProductsList(generics.ListAPIView):
	"""
    List all the products of the logged Store Admin Store, PERMISSION: Only Store Admins
    """
	serializer_class = ProductSerializer

	def get_queryset(self):
		store = Store.objects.get(pk=self.kwargs['pk'])
		return store.product_set.all()

class StoreDeliveryList(generics.ListCreateAPIView):
	"""
    List the Delivery days available in the Store (DAYS(HOURS OF OPERATION))
    """

	serializer_class = DeliverySerializer

	def get_queryset(self):
		store = Store.objects.get(pk=self.kwargs['pk'])
		return Delivery.objects.all().filter(store=store)

	def perform_create(self, serializer):
		store = Store.objects.get(pk=self.kwargs['pk'])
		serializer.save(store=store)

class StoreDeliveryDay(generics.ListCreateAPIView):
	"""
    List the Store's Delivery Days from the logged Store Admin
    """

	serializer_class = DeliveryDaySerializer

	def get_queryset(self):
		store = Store.objects.get(pk=self.kwargs['pk'])
		delivery_days = DeliveryDay.objects.all().filter(delivery=store.delivery)
		return delivery_days

	def perform_create(self, serializer):
		store = Store.objects.get(pk=self.kwargs['pk'])
		serializer.save(delivery=store.delivery)

class StoreDeliveryHour(generics.CreateAPIView):
	"""
    List the Store's Delivery Days hours from the logged Store Admin
    """
	serializer_class = DeliveryHourSerializer

	def perform_create(self, serializer):
		delivery_day = DeliveryDay.objects.get(pk=self.kwargs['pk'])
		serializer.save(delivery_day=delivery_day)