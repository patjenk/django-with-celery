from __future__ import absolute_import

from bs4 import BeautifulSoup
from celery import shared_task
from datetime import datetime
import requests

from .models import Temperature


@shared_task
def lookup_baltimore_temperature(temperature_request_id):
    temperature_request = Temperature.objects.get(id=temperature_request_id)
    url = "http://www.accuweather.com/en/us/baltimore-md/21230/weather-forecast/8872_pc"
    temperature_request.temperature_f  = scrape_accuweather(url)
    temperature_request.response_datetime = datetime.now()
    temperature_request.save()

def lookup_hawi_temperature():
    url = "http://www.accuweather.com/en/us/hawi-hi/96743/weather-forecast/332597"
    return scrape_accuweather(url)

def lookup_woodshole_temperature():
    url = "http://www.accuweather.com/en/us/woods-hole-ma/02543/weather-forecast/2089379"
    return scrape_accuweather(url)

def scrape_accuweather(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    temp = soup.find_all("strong", {"class": "temp"})[0].contents[0]
    return temp
