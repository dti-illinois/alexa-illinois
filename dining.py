import json
import urllib
import requests
from urllib.request import urlopen

hall_id = {
    'lar': 5,
    'fieldofgreens': 12,
    'leafy': 13,
    'par': 2,
    'pennstation': 14,
    'isr': 3,
    'chomps': 18,
    'cocinamexicana': 10,
    'tasteofasia': 17,
    'ikenberrydininghall': 1,
    '57north': 7,
    'betterburger': 20,
    'caffeinator': 9,
    'neosoulingredient': 21,
    'far': 6,
    'crackedeggcafe': 8,
    'soulingredient': 16,
    'buseyevans': 4,
    'buseybeanandgreen': 11,
    'oodles': 19
}

url_dining_today = "https://web.housing.illinois.edu/MobileDining2/WebService/Search.aspx?k=7A828F94-620B-4EE3-A56F-328036CC3C04"
url_dining_search = "https://web.housing.illinois.edu/MobileDining/WebService/MobileDining.asmx/SearchMenus?k=7A828F94-620B-4EE3-A56F-328036CC3C04&SearchPhrase="

def get_hall_id(hall_name):
    return hall_id[hall_name]


def get_dining_today(hall, meal, course):
    request_url = url_dining_today + "&id=" + str(hall) + "&t=json"
    response = urlopen(request_url)
    try:
        response_json = json.load(response)
        items = response_json['Menus']['Item']
        results = []
        for item in items:
            if item['Course'] == course and item['Meal'] == meal:
                results.append(item['FormalName'])
        return results
    except ValueError:
        return None