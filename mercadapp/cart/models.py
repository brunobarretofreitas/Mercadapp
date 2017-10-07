# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Cart(models.Model):
	store = models.ForeignKey('market.Store', default='', on_delete=models.CASCADE)
	user = models.ForeignKey(User, default='')

	def __str__(self):
		return self.user.username + " : " + self.store.name

class CartItem(models.Model):
	product = models.ForeignKey('product.Product', default='')
	cart = models.ForeignKey(Cart, related_name='cart_items', default= '')

	def __str__(self):
		return self.product.name
