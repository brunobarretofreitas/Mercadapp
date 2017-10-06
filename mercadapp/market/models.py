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
	logo = models.CharField(max_length=200, blank=False)
	minimum_order = models.FloatField()
	delivery_tax = models.FloatField()
	delivery_radius = models.FloatField()

	def __str__(self):
		return self.name

	def can_deliver(self, client_zip_code):
		distance = Distance().get_distance_between(client_zip_code, str(self.zip_code))
		return True if distance <= self.delivery_radius else False

class DeliveryTime(models.Model):
	store = models.ForeignKey(Store, on_delete=models.CASCADE, default='')
	day_of_the_week = models.IntegerField(
		choices=DAYS_OF_THE_WEEK,
		default=1
	)

	def __str__(self):
		return self.day_of_the_week

class DeliveryHour(models.Model):
	delivery_time = models.ForeignKey(DeliveryTime, on_delete=models.CASCADE, default='')
	initial_hour = models.TimeField()
	end_hour = models.TimeField()

	def __str__(self):
		return self.initial_hour + " : " + self.end_hour

class Product(models.Model):
	name = models.CharField(max_length=200, default='', blank=False)
	value = models.FloatField()
	store = models.ForeignKey(Store, on_delete=models.CASCADE, default='')

	def __str__(self):
		return self.id

DELIVERY_MISSED_PRODUCTS_OPTIONS = (
    ('RC', 'Receive calling to decide'),
    ('RP', 'Replace missing products with a similar product or price')
)


class Order(models.Model):
	store = models.ForeignKey(Store, on_delete=models.CASCADE)
	products = models.ManyToManyField(Product)
	value = models.FloatField()
	order_date = models.DateField(auto_now=True)
	was_delivered = models.BooleanField(default=False)

	def __str__(self):
		return self.store.name + " : " + self.value

class Delivery(models.Model):
	order = models.ForeignKey(Order, default='', on_delete=models.CASCADE)
	delivery_date = models.DateTimeField()
	client_name = models.CharField(max_length=100, blank=False)
	cpf = models.CharField(max_length=11, blank=False)
	telephone = models.CharField(max_length=20, default='')
	email = models.EmailField(max_length=254)
	zip_code = models.CharField(max_length=9, blank=False)
	street = models.CharField(max_length=300, blank=False)
	house_number = models.CharField(max_length=10, blank=False)
	complement = models.CharField(max_length=500)
	reference_point = models.CharField(max_length=500)
	neighborhood = models.CharField(max_length=200)
	delivery_note = models.TextField()
	delivery_missed_products = models.CharField(
		max_length=2,
		choices=DELIVERY_MISSED_PRODUCTS_OPTIONS,
		default='RC'
	)

	def __str__(self):
		return self.client_name + " : " + self.street
