# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-22 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oneliners', '0005_auto_20160222_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='context',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
