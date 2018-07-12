import json
import time
import urllib
import requests

from urllib.request import urlopen
from datetime import date
from datetime import timedelta

url_library_all = "https://quest.library.illinois.edu/LibDirectory/Api/UnitsWithCalendars"
url_library_search = "https://quest.library.illinois.edu/LibDirectory/Api/SearchCalendar/"

path_model = "model.json"
path_slot_library = "data/slot_library.json"


def get_library_id(response):
    results = {}
    for item in response_json:
        results[item["unit_name"]] = item["library_number"]
    return results


def get_catalog():
    results = []
    model = json.load(open(path_model, 'r'))
    for slot in model["interactionModel"]["languageModel"]["types"][0]["values"]:
        results.append(slot["name"]["value"])
    return results


def get_all():
    request_url = url_library_all
    response_json = urlopen(request_url)
    try:
        response = json.load(response_json)
        return response
    except ValueError:
        return None


def get_calendar(library_id, y, m, d):
    request_url = url_library_search + str(library_id) + "/" + y + "/" + m + "/" + d
    print(request_url)
    response_json = urlopen(request_url)
    try:
        response = json.load(response_json)
        return response
    except ValueError:
        return None

