# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 16:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('market', '0005_auto_20171006_0216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='market.Cart')),
                ('product', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='market.Product')),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_day', models.IntegerField(choices=[(1, 'Sunday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday')], default=1)),
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
                ('status', models.CharField(choices=[('N', 'New'), ('A', 'Approved'), ('S', 'Sent'), ('D', 'Delivered')], default='N', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='deliverytime',
            name='store',
        ),
        migrations.RemoveField(
            model_name='delivery',
            name='client_name',
        ),
        migrations.RemoveField(
            model_name='delivery',
            name='complement',
        ),
        migrations.RemoveField(
            model_name='delivery',
            name='cpf',
        ),
        migrations.RemoveField(
            model_name='delivery',
            name='delivery_date',
        ),
        migrations.RemoveField(
            model_name='delivery',
            name='delivery_missed_products',
        ),
        migrations.RemoveField(
            model_name='delivery',
            name='delivery_note',
        ),
        migrations.RemoveField(
            model_name='delivery',
            name='email',
        ),
        migrations.RemoveField(
            model_name='delivery',
            name='house_number',
        ),
        migrations.RemoveField(
            model_name='delivery',
            name='neighborhood',
        ),
        migrations.RemoveField(
            model_name='delivery',
            name='order',
        ),
        migrations.RemoveField(
            model_name='delivery',
            name='reference_point',
        ),
        migrations.RemoveField(
            model_name='delivery',
            name='street',
        ),
        migrations.RemoveField(
            model_name='delivery',
            name='telephone',
        ),
        migrations.RemoveField(
            model_name='delivery',
            name='zip_code',
        ),
        migrations.RemoveField(
            model_name='deliveryhour',
            name='delivery_time',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.RemoveField(
            model_name='order',
            name='store',
        ),
        migrations.RemoveField(
            model_name='order',
            name='value',
        ),
        migrations.RemoveField(
            model_name='order',
            name='was_delivered',
        ),
        migrations.RemoveField(
            model_name='store',
            name='logo',
        ),
        migrations.AddField(
            model_name='delivery',
            name='store',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='market.Store'),
        ),
        migrations.DeleteModel(
            name='DeliveryTime',
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='order',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='market.Order'),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='payment',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='market.Payment'),
        ),
        migrations.AddField(
            model_name='cart',
            name='store',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='market.Store'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='deliveryhour',
            name='delivery_day',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='market.DeliveryDay'),
        ),
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='market.Cart'),
        ),
    ]