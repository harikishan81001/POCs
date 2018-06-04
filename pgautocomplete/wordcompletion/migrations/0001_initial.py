# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-31 19:04
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('client_id', models.IntegerField()),
                ('address', django.contrib.postgres.fields.jsonb.JSONField()),
                ('active', models.BooleanField(default=True)),
                ('center_type', models.CharField(choices=[('PCK', 'PickUp'), ('DRP', 'DROP')], default='PCK', max_length=10)),
                ('location_type', models.CharField(choices=[('HM', 'HOME'), ('OFF', 'OFFICE')], default='HM', max_length=10)),
            ],
        ),
    ]
