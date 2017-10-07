# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 19:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0008_auto_20171006_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='market.Cart'),
        ),
    ]