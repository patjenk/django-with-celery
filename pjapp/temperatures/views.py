from datetime import datetime
from django.shortcuts import HttpResponse
from django.template import loader
import json

from . import tasks
from .models import Temperature


def index(request):
    temperature_lookups = Temperature.objects.order_by('-request_datetime')[:20]
    for temperature_lookup in temperature_lookups:
        if temperature_lookup.response_datetime is not None:
            fullfillment_timedelta = (temperature_lookup.response_datetime -temperature_lookup.request_datetime)
            temperature_lookup.fulfillment_seconds = fullfillment_timedelta.seconds
        else:
            temperature_lookup.fulfillment_seconds = None
    template = loader.get_template("temperatures/index.html")
    context = {
        'temperature_lookups': temperature_lookups,
    }
    return HttpResponse(template.render(context, request))


def baltimore_temperature(request):
    new_temperature_request = Temperature(request_datetime=datetime.now(), location="Baltimore, MD", temperature_f=None, response_datetime=None, type_of_request="Asynchronous Task")
    new_temperature_request.save()
    tasks.lookup_baltimore_temperature.apply_async((new_temperature_request.id,), countdown=5)
    result = { "result": "requested" }
    return HttpResponse(json.dumps(result), content_type="application/json")
