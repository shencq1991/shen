# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-08 05:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Echarts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Xb', models.CharField(max_length=20)),
                ('num', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('code', models.CharField(max_length=20)),
                ('industry', models.TextField()),
                ('province', models.CharField(max_length=20)),
                ('created_date', models.TextField()),
                ('address', models.TextField()),
                ('author', models.CharField(default='wm-station', max_length=20)),
                ('update_time', models.DateTimeField(default=datetime.datetime.now)),
                ('date', models.TextField()),
                ('net_profits', models.TextField()),
                ('esp', models.TextField()),
                ('business_income', models.TextField()),
                ('bips', models.TextField()),
                ('Asset', models.TextField()),
                ('scale', models.TextField()),
                ('roe_yoy', models.TextField()),
                ('esp_yoy', models.TextField()),
                ('bvps', models.TextField()),
                ('epcf', models.TextField()),
                ('profits_yoy', models.TextField()),
                ('roe', models.TextField()),
                ('net_profit_ratio', models.TextField()),
                ('gross_profit_rate', models.TextField()),
                ('arturnover', models.TextField()),
                ('inventory_turnover', models.TextField()),
                ('currentasset_turnover', models.TextField()),
                ('business_income_yoy', models.TextField()),
                ('nav', models.TextField()),
                ('targ', models.TextField()),
                ('epsg', models.TextField()),
                ('currentratio', models.TextField()),
                ('quickratio', models.TextField()),
                ('cashratio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post300',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('code', models.CharField(max_length=20)),
                ('industry', models.TextField()),
                ('province', models.CharField(max_length=20)),
                ('created_date', models.TextField()),
                ('address', models.TextField()),
                ('author', models.CharField(default='wm-station', max_length=20)),
                ('update_time', models.DateTimeField(default=datetime.datetime.now)),
                ('date', models.TextField()),
                ('net_profits', models.TextField()),
                ('esp', models.TextField()),
                ('business_income', models.TextField()),
                ('bips', models.TextField()),
                ('Asset', models.TextField()),
                ('scale', models.TextField()),
                ('roe_yoy', models.TextField()),
                ('esp_yoy', models.TextField()),
                ('bvps', models.TextField()),
                ('epcf', models.TextField()),
                ('profits_yoy', models.TextField()),
                ('roe', models.TextField()),
                ('net_profit_ratio', models.TextField()),
                ('gross_profit_rate', models.TextField()),
                ('arturnover', models.TextField()),
                ('inventory_turnover', models.TextField()),
                ('currentasset_turnover', models.TextField()),
                ('business_income_yoy', models.TextField()),
                ('nav', models.TextField()),
                ('targ', models.TextField()),
                ('epsg', models.TextField()),
                ('currentratio', models.TextField()),
                ('quickratio', models.TextField()),
                ('cashratio', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]