# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-23 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0010_auto_20170823_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='First_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='Last_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]