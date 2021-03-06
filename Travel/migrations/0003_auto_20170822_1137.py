# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-22 08:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0002_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('QUOTE', 'quote'), ('IN PROCESS', 'in process'), ('BOOKED', 'booked')], max_length=100, null=True),
        ),
    ]
