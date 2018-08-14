from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import json

from consts import LaundryConsts

url = "https://69smoo2dc6.execute-api.us-east-1.amazonaws.com/api/laundry"

def get_building_id(building_name) :
	return LaundryConsts.building_id[building_name]

def general_search():
	return json.loads(urlopen(url).read().decode('utf-8'))

def get_supported_buildings():
	buildings = []
	for key in LaundryConsts.building_id_matcher:
		buildings.append(LaundryConsts.building_id_matcher[key])
	return buildings

def get_specific_slots(building_id, machine) :
	data = general_search()
	for building in data:
		if LaundryConsts.building_id_matcher[building_id] == building['building']:
			return building[machine]
	return None
