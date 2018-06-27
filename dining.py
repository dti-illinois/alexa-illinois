import json
import urllib
import requests
from urllib.request import urlopen

hall_id = {
    
}

url_dining_today = "https://web.housing.illinois.edu/MobileDining2/WebService/Search.aspx?k=7A828F94-620B-4EE3-A56F-328036CC3C04"
url_dining_search = "https://web.housing.illinois.edu/MobileDining/WebService/MobileDining.asmx/SearchMenus?k=7A828F94-620B-4EE3-A56F-328036CC3C04&SearchPhrase="

def get_hall_id(hall_name):



def get_dining_today(hall, meal, course):
    request_url = url_dining_today + "&id=" + hall + "&t=json"
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