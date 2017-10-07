# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticated, AllowAny
from mercadapp.permissions import IsStoreAdmin, IsClient
from rest_framework import generics

from .serializers import UserSerializer

from django.shortcuts import render
from order.serializers import OrderSerializer
from cart.serializers import CartSerializer
from order.models import Order
from cart.models import Cart,CartItem
# Create your views here.
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

class UserDetail(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

class UserOrders(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = (IsClient,)
    
    def get_queryset(self):
        user = self.request.user
        orders = Order.objects.all().filter(client=user)
        return orders

    def perform_create(self, serializer):
        user = self.request.user
        cart = Cart.objects.get(pk=self.request.POST.get("cart",1))
        cart_items = CartItem.objects.all().filter(cart=cart)
        value = 0
        for item in cart_items:
            value += item.product.value

        serializer.save(client=user, store=cart.store, value=value)

class UserCarts(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    permission_classes = (IsClient,)
    
    def get_queryset(self):
        user = self.request.user
        carts = Cart.objects.all().filter(user=user)
        return carts

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)