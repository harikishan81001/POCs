# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-01 08:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordcompletion', '0007_auto_20180601_0757'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookscatalog',
            old_name='publication',
            new_name='seller',
        ),
        migrations.AlterField(
            model_name='bookscatalog',
            name='uuid',
            field=models.CharField(default=b'2d196aaaebbf4fed925a554a77cc095c', max_length=50),
        ),
    ]
