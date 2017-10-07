# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics

from django.shortcuts import render

from .models import Product
from .serializers import ProductSerializer
from market.models import Store
from mercadapp.permissions import IsStoreAdmin, IsClient

# Create your views here.
class ProductList(generics.ListCreateAPIView):
	serializer_class = ProductSerializer
	permission_classes = (IsStoreAdmin,)

	def get_queryset(self):
		user = self.request.user
		store = Store.objects.get(store_admin=user)
		return store.product_set.all()

	def perform_create(self, serializer):
		user = self.request.user
		store = Store.objects.get(store_admin=user)
		serializer.save(store=store)

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer