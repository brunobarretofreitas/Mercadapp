# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 16:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0007_deliveryday_store'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deliveryday',
            old_name='store',
            new_name='delivery',
        ),
    ]