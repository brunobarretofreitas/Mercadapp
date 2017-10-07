# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import cart
from django.contrib.auth.models import User

# Create your models here.
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
	store = models.ForeignKey('market.Store', default='')
	client = models.ForeignKey(User, default='')
	cart = models.ForeignKey('cart.Cart', default='')
	status = models.CharField(
		max_length=1,
		choices=ORDER_STATUS,
		default='N')
	value = models.FloatField(default=0)

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