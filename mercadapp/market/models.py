# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from .distance import Distance

# Create your models here.
DAYS_OF_THE_WEEK = (
	(1, 'Sunday'),
	(2, 'Tuesday'),
	(3, 'Wednesday'),
	(4, 'Thursday'),
	(5, 'Friday'),
	(6, 'Saturday')
)

class Store(models.Model):
	store_admin = models.OneToOneField(User, default='')
	name = models.CharField(max_length=100, blank=False)
	description = models.TextField()
	zip_code = models.CharField(max_length=9, blank=False)
	telephone = models.CharField(max_length=30, default='')
	email = models.EmailField(max_length=254)
	minimum_order = models.FloatField()
	delivery_tax = models.FloatField()
	delivery_radius = models.FloatField()

	def __str__(self):
		return self.name
		
	def can_deliver(self, client_zip_code):
		distance = Distance().get_distance_between(client_zip_code, str(self.zip_code))
		return True if distance <= self.delivery_radius else False


class Product(models.Model):
	name = models.CharField(max_length=200, default='', blank=False)
	value = models.FloatField()
	store = models.ForeignKey(Store, on_delete=models.CASCADE, default='')

	def __str__(self):
		return self.name

class Cart(models.Model):
	store = models.ForeignKey(Store, default='', on_delete=models.CASCADE)
	user = models.ForeignKey(User, default='')

	def __str__(self):
		return self.user.username + " : " + self.store.name

class CartItem(models.Model):
	product = models.OneToOneField(Product, default='')
	cart = models.ForeignKey(Cart, related_name='cart_items', default= '')

	def __str__(self):
		return self.product.name

class Payment(models.Model):
	name = models.CharField(max_length=100, default='')

	def __str__(self):
		return self.name


ORDER_STATUS = (
	('N', 'New'),
	('A', 'Approved'),
	('S', 'Sent'),
	('D', 'Delivered'),
)


class Order(models.Model):
	cart = models.ForeignKey(Cart, default='')
	status = models.CharField(
		max_length=1,
		choices=ORDER_STATUS,
		default='N')

	def __str__(self):
		return self.cart.store.name + ":"+self.cart.user.username


class OrderInfo(models.Model):
	order = models.OneToOneField(Order, related_name='order_info', default='', on_delete=models.CASCADE)
	street = models.CharField(max_length=300, blank=False)
	house_number = models.CharField(max_length=10, blank=False)
	complement = models.CharField(max_length=500)
	reference_point = models.CharField(max_length=500)
	neighborhood = models.CharField(max_length=200)
	delivery_note = models.TextField()
	payment = models.ForeignKey(Payment, default='')

	def __str__(self):
		return self.status


class Delivery(models.Model):
	store = models.OneToOneField(Store, default='')

	def __str__(self):
		return self.store.name

class DeliveryDay(models.Model):
	delivery = models.ForeignKey(Delivery, related_name='delivery_days', default='')
	week_day = models.IntegerField(
		choices=DAYS_OF_THE_WEEK,
		default=1,
		unique=True
	)

	def __str__(self):
		return self.week_day

class DeliveryHour(models.Model):
	delivery_day = models.OneToOneField(DeliveryDay, related_name='delivery_hour', default='')
	initial_hour = models.TimeField()
	end_hour = models.TimeField()

	def __str__(self):
		return self.initial_hour + " - " + self.end_hour