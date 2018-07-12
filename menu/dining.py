import json
import time
import urllib
import requests
from urllib.request import urlopen
from datetime import date
from datetime import timedelta


url_dining = "https://web.housing.illinois.edu/MobileDining2/WebService/Search.aspx?k=7A828F94-620B-4EE3-A56F-328036CC3C04"
url_dining_search = "https://web.housing.illinois.edu/MobileDining/WebService/MobileDining.asmx/SearchMenus?k=7A828F94-620B-4EE3-A56F-328036CC3C04&SearchPhrase="

hall_id = {
    'ikenberrydininghall': 1,
    'par': 2,
    'isr': 3,
    'buseyevans': 4,
    'lar': 5,
    'far': 6,
    '57north': 7,
    'crackedeggcafe': 8,
    'caffeinator': 9,
    'cocinamexicana': 10,
    'buseybeanandgreen': 11,
    'fieldofgreens': 12,
    'leafy': 13,
    'pennstation': 14,
    'soulingredient': 16,
    'tasteofasia': 17,
    'chomps': 18,
    'oodles': 19,
    'betterburger': 20,
    'neosoulingredient': 21,
}


def get_hall_id(hall_name):
    return hall_id[hall_name]


def get_tomorrow_url():
    tmr = date.today() + timedelta(days=1)
    tmr_str = tmr.strftime("%Y-%m-%d")
    return url_dining + "&from=" + tmr_str + "&to=" + tmr_str


def get_dining(date, hall, meal, course, filters):
    if date =='today':
        request_url = url_dining + "&id=" + str(hall) + "&t=json"
    elif date == 'tomorrow':
        request_url = get_tomorrow_url() + "&id=" + str(hall) + "&t=json"
    else:
        return None
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