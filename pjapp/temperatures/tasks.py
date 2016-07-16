from __future__ import absolute_import

from bs4 import BeautifulSoup
from celery import shared_task
from celery.task import periodic_task
from datetime import datetime, timedelta
import requests

from .models import Temperature


@shared_task
def lookup_baltimore_temperature(temperature_request_id):
    temperature_request = Temperature.objects.get(id=temperature_request_id)
    url = "http://www.accuweather.com/en/us/baltimore-md/21230/weather-forecast/8872_pc"
    temperature_request.temperature_f  = scrape_accuweather(url)
    temperature_request.response_datetime = datetime.now()
    temperature_request.save()


@periodic_task(run_every=timedelta(minutes=1))
def lookup_hawi_temperature():
    temperature_request = Temperature(request_datetime=datetime.now(), location="Hawi, HI", temperature_f=None, response_datetime=None, type_of_request="Periodic Task")
    url = "http://www.accuweather.com/en/us/hawi-hi/96743/weather-forecast/332597"
    temperature_request.temperature_f  = scrape_accuweather(url)
    temperature_request.response_datetime = datetime.now()
    temperature_request.save()


@periodic_task(run_every=timedelta(minutes=5))
def lookup_woodshole_temperature():
    temperature_request = Temperature(request_datetime=datetime.now(), location="Woods Hole, MA", temperature_f=None, response_datetime=None, type_of_request="Periodic Task")
    url = "http://www.accuweather.com/en/us/woods-hole-ma/02543/weather-forecast/2089379"
    temperature_request.temperature_f  = scrape_accuweather(url)
    temperature_request.response_datetime = datetime.now()
    temperature_request.save()


def scrape_accuweather(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    temp = soup.find_all("strong", {"class": "temp"})[0].contents[0]
    return temp
