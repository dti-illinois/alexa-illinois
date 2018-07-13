import json
import time
import urllib
import requests

from urllib.request import urlopen
from datetime import date
from datetime import timedelta
from datetime import datetime

url_library_all = "https://quest.library.illinois.edu/LibDirectory/Api/UnitsWithCalendars"
url_library_search = "https://quest.library.illinois.edu/LibDirectory/Api/SearchCalendar/"

path_model = "model.json"
path_slot_library = "data/slot_library.json"

weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


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

def process_next_seven_days(calendar):
    dates, labels, until = [], [], [0] * 7
    flag_next_week = False
    for i in range(7):
        oneday = datetime.strptime(calendar['nextSevenDays'][i]['date'], "%m/%d/%Y")
        if oneday.weekday() == 0:
            flag_next_week = True
        if flag_next_week:
            dates.append("next " + weekday[oneday.weekday()])
        else:
            dates.append(weekday[oneday.weekday()])
        labels.append(calendar['nextSevenDays'][i]['hours'][0]['label'])
    dates[0], dates[1] = 'today', 'tomorrow'
    # look for intervals
    for i in range(7):
        for j in range(i, 7):
            if labels[j] != labels[i]: break
            until[i] = j
    # use pointer to contruct intervals
    date_from, date_to, opening_hours = [], [], []
    ptr_start = 0
    while (ptr_start < 7):
        date_from.append(dates[ptr_start])
        date_to.append(dates[until[ptr_start]])
        opening_hours.append(labels[ptr_start])
        ptr_start = until[ptr_start] + 1
    return date_from, date_to, opening_hours