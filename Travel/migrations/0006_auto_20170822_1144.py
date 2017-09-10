# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-22 08:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0005_order_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='destination',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('QUOTE', 'Quote'), ('IN PROCESS', 'In process'), ('BOOKED', 'Booked')], max_length=100, null=True),
        ),
    ]
