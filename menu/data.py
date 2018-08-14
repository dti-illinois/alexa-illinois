import json
import time
import urllib
import requests
from urllib.request import urlopen
from datetime import date
from datetime import timedelta


url_dining = "https://69smoo2dc6.execute-api.us-east-1.amazonaws.com/api/dining"


def get_tomorrow_url(hall):
    tmr = date.today() + timedelta(days=1)
    tmr_str = tmr.strftime("%Y-%m-%d")
    return url_dining + "/" + hall + "/" + tmr_str + "/" + tmr_str


def get_dining(date, hall, meal, course, filters):
    if date =='today':
        request_url = url_dining + "/" + hall
    elif date == 'tomorrow':
        request_url = get_tomorrow_url(hall)
    else:
        return None
    print(request_url)
    response = urlopen(request_url)
    try:
        response_json = json.load(response)
        items = response_json['Menus']['Item']
        results = []
        for item in items:
            if item['Course'] == course and item['Meal'] == meal:
                flag = True
                for tag in filters.keys():
                    if filters[tag]:
                        if tag == "Gluten-free":
                            if "Gluten" in item['Traits'].split(','): 
                                flag = False
                        elif filters[tag] and tag not in item['Traits'].split(','):
                            flag = False
                if flag and item['FormalName'] not in results:
                    results.append(item['FormalName'])
        return results
    except ValueError:
        return None