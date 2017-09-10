# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-22 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0003_auto_20170822_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('QUOTE', 'Quote'), ('IN PROCESS', 'In process'), ('BOOKED', 'Booked')], max_length=100, null=True),
        ),
    ]
