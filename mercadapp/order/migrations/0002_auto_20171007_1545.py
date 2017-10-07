# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 15:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('market', '0014_auto_20171007_1441'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='client',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='store',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='market.Store'),
        ),
    ]