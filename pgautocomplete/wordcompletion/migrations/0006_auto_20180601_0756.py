# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-01 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordcompletion', '0005_bookscatalog_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookscatalog',
            name='uuid',
            field=models.CharField(default=b'0f37663f6fef4bff958afa6c6058b096', max_length=30),
        ),
    ]
