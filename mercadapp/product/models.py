# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import market

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=200, default='', blank=False)
	value = models.FloatField()
	store = models.ForeignKey(market.models.Store, on_delete=models.CASCADE, default='')

	def __str__(self):
		return self.name