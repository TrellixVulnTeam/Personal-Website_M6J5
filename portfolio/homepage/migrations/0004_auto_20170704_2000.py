# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-04 19:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20170704_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepagelink',
            name='optional_class',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='homepagelink',
            name='link_description',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
