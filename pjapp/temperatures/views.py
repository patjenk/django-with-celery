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
    result = {"temperature": tasks.lookup_baltimore_temperature() }
    return HttpResponse(json.dumps(result), content_type="application/json")

def hawi_temperature(request):
    result = {"temperature": tasks.lookup_hawi_temperature() }
    return HttpResponse(json.dumps(result), content_type="application/json")

def woodshole_temperature(request):
    result = {"temperature": tasks.lookup_woodshole_temperature() }
    return HttpResponse(json.dumps(result), content_type="application/json")
