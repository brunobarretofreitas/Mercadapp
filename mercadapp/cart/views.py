# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics

from .serializers import CartSerializer, CartItemSerializer

from .models import *
# Create your views here.
class CreateCart(generics.CreateAPIView):
	serializer_class = CartSerializer

	def perform_create(self, serializer):
		user = self.request.user
		serializer.save(user=user)

class CartDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Cart.objects.all()
	serializer_class = CartSerializer

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