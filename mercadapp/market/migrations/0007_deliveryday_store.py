# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 16:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0006_auto_20171006_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryday',
            name='store',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='market.Delivery'),
        ),
    ]