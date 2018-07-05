import json
import urllib
import requests
from urllib.request import urlopen


url_dining_today = "https://web.housing.illinois.edu/MobileDining2/WebService/Search.aspx?k=7A828F94-620B-4EE3-A56F-328036CC3C04"
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


def get_dining_today(hall, meal, course):
    request_url = url_dining_today + "&id=" + str(hall) + "&t=json"
    response = urlopen(request_url)
    try:
        response_json = json.load(response)
        items = response_jsoSn['Menus']['Item']
        results = []
        for item in items:
            if item['Course'] == course and item['Meal'] == meal:
                results.append(item['FormalName'])
        return results
    except ValueError:
        return None


def get_dining_tomorrow(hall, meal, course):
    request_url = url_dining_today + "&id=" + str(hall) + "&t=json"
    response = urlopen(request_url)
    try:
        response_json = json.load(response)
        items = response_jsoSn['Menus']['Item']
        results = []
        for item in items:
            if item['Course'] == course and item['Meal'] == meal:
                results.append(item['FormalName'])
        return results
    except ValueError:
        return None