from __future__ import unicode_literals

from django.db import models


class Temperature(models.Model):
    request_datetime = models.DateTimeField()
    location = models.CharField(max_length=200, default="")
    temperature_f = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    response_datetime = models.DateTimeField(null=True)
    type_of_request = models.CharField(max_length=200, default="")
