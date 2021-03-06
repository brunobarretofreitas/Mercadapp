# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 14:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('N', 'New'), ('A', 'Approved'), ('S', 'Sent'), ('D', 'Delivered')], default='N', max_length=1)),
                ('cart', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cart.Cart')),
            ],
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=300)),
                ('house_number', models.CharField(max_length=10)),
                ('complement', models.CharField(max_length=500)),
                ('reference_point', models.CharField(max_length=500)),
                ('neighborhood', models.CharField(max_length=200)),
                ('delivery_note', models.TextField()),
                ('order', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='order_info', to='order.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='payment',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='order.Payment'),
        ),
    ]
