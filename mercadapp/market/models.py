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
	store_admin = models.OneToOneField(User, related_name='store', default='')
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