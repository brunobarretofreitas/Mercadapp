# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 19:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='product.Product'),
        ),
    ]
