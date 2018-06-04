# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.shortcuts import render
from django.http import JsonResponse
from django.db import connections


def index(request):
    return render(request, 'index.html')


def get_data(request):
    query = request.GET.get("query")
    if not query:
        return []

    active = request.GET.get("active")
    if active in ["true", "false"]:
        active = True if active == "true" else False

    incoming_center = request.GET.get("incoming_center")
    query = (
        "SELECT * FROM wordcompletion_warehouses"
        " WHERE name LIKE '%{query}%'".format(query=query))

    if active in [True, False]:
        query = query + " AND active={active}".format(active=active)

    if incoming_center:
        query = query + " AND incoming_center='{incoming_center}'".format(
            incoming_center=incoming_center)

    cursor = connections["default"].cursor()

    print query
    cursor.execute(query)
    data = [dict((cursor.description[i][0], value) for
                 i, value in enumerate(row)) for row in cursor.fetchall()]

    resp = []
    for each in data:
        resp.append({"value": each["name"], "data": each})

    return JsonResponse(resp, safe=False)
