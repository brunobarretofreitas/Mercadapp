# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework import generics

from django.shortcuts import render
from .serializers import StoreSerializer, ProductSerializer, UserSerializer
from .models import Store, Product

# Create your views here.
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
    	serializer.save(store_admin=self.request.user)

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class StoreList(generics.ListCreateAPIView):
	queryset = Store.objects.all()
	serializer_class = StoreSerializer

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
		store = Store.objects.get(pk=self.kwargs['pk'])
		serializer.save(store=store)

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = ProductSerializer

	def get_queryset(self):
		product = Product.objects.all().filter(pk=self.kwargs['product'])
		return product