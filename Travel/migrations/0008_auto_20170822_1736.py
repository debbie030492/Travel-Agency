# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-22 14:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0007_auto_20170822_1241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customer',
            new_name='Customer',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='date',
            new_name='Date',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='dep_city',
            new_name='Departing_city',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='destination',
            new_name='Destination',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='notes',
            new_name='Notes',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='nb_people',
            new_name='Number_of_travelers',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='package',
            new_name='Package',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='price',
            new_name='Price',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='status',
            new_name='Status',
        ),
    ]
