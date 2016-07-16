from datetime import datetime
from django.shortcuts import HttpResponse
from django.template import loader
import json

from . import tasks
from .models import Temperature


def index(request):
    temperature_lookups = Temperature.objects.order_by('-request_datetime')[:20]
    template = loader.get_template("temperatures/index.html")
    context = {
        'temperature_lookups': temperature_lookups,
    }
    return HttpResponse(template.render(context, request))

def baltimore_temperature(request):
    new_temperature_request = Temperature(request_datetime=datetime.now(), location="Baltimore, MD", temperature_f=None, response_datetime=None, type_of_request="CeleryD")
    new_temperature_request.save()
    tasks.lookup_baltimore_temperature.apply((new_temperature_request.id,), delay=10)
    result = { "result": "requested" }
    return HttpResponse(json.dumps(result), content_type="application/json")

def hawi_temperature(request):
    result = {"temperature": tasks.lookup_hawi_temperature() }
    return HttpResponse(json.dumps(result), content_type="application/json")

def woodshole_temperature(request):
    result = {"temperature": tasks.lookup_woodshole_temperature() }
    return HttpResponse(json.dumps(result), content_type="application/json")
