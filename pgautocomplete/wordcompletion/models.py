# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.contrib.postgres.fields import JSONField
from django.db import models


def get_uuid():
    return uuid.uuid4().hex


class Warehouses(models.Model):
    uuid = models.CharField(max_length=50, default=get_uuid())
    name = models.CharField(max_length=255, null=False, blank=False)
    registered_name = models.CharField(max_length=255)
    seller_id = models.CharField(max_length=255, null=True)
    address = JSONField()
    incoming_center = models.CharField(max_length=40)
    rto_center = models.CharField(max_length=40)
    dto_center = models.CharField(max_length=40)
    active = models.BooleanField(default=True)
    pin_code = models.CharField(max_length=10, null=False)

    def __unicode__(self):
        return (
            "<Class Warehouses <{}:{}>>".format(
                self.name, self.seller_id))
