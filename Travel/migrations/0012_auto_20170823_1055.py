# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-23 07:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0011_auto_20170823_1045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='Date',
            new_name='Date_of_departure',
        ),
    ]
