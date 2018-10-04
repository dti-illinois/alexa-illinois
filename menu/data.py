import json
import time
import urllib2

from urllib2 import urlopen
from datetime import date
from datetime import timedelta


url_dining = "https://web.housing.illinois.edu/MobileDining2/WebService/Search.aspx?id="


def get_tomorrow_url(hall_id):
    tmr = date.today() + timedelta(days=1)
    tmr_str = tmr.strftime("%m/%d/%Y")
    return url_dining + hall_id + "&from=" + tmr_str + "&to=" + tmr_str + "&t=json&k=7A828F94-620B-4EE3-A56F-328036CC3C04"

def get_today_url(hall_id):
    tmr = date.today()
    tmr_str = tmr.strftime("%m/%d/%Y")
    return url_dining + hall_id + "&from=" + tmr_str + "&to=" + tmr_str + "&t=json&k=7A828F94-620B-4EE3-A56F-328036CC3C04"

def get_dining(date, hall_id, meal, course, filters):
    url_dining = get_today_url(hall_id)
    response = urlopen(url_dining)
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