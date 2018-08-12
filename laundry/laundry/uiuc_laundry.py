import json
import urllib
from urllib2 import urlopen
from bs4 import BeautifulSoup
import requests
import re

building_id = {
	'allen' : 1,
	'bousefield' : 2,
	'busey' : 3,
	'clark' : 4,
	'daniels' : 5,
	'f.a.r' : 6,
	'goodwingreen' : 7,
	'hopkins' : 8,
	'i.s.r' : 9,
	'l.a.r' : 10,
	'nugent' : 11,
	'orcharddowns' : 12,
	'p.a.r' : 13,
	'scott' : 14,
	'sherman' : 15,
	'snyder' : 16,
	'tvd' : 17,
	'wassaja' : 18,
	'weston' : 19
}

building_id_matcher = {
	1 : 'allen',
	2 : 'bousefield',
	3 : 'busey',
	4 : 'clark',
	5 : 'daniels',
	6 : 'f.a.r',
	7 : 'goodwingreen',
	8 : 'hopkins',
	9 : 'i.s.r',
	10 : 'l.a.r',
	11 : 'nugent',
	12 : 'orcharddowns',
	13 : 'p.a.r',
	14 : 'scott',
	15 : 'sherman',
	16 : 'snyder',
	17 : 'tvd',
	18 : 'wassaja',
	19 : 'weston'
}
building_room_matcher = {
	1 : 'room 49',
	2 : ['room 101', 'room 103'],
	3 : 'room 8',
	4 : 'room 30',
	5 : ['north room 11', 'south room 40'],
	6 : ['oglesby room 1', 'trelease room 13'],
	7 : ['green room 31', 'goodwin room 8'],
	8 : ['room 150'],
	9 : ['townsend room 35', 'wardall room 12'],
	10 : ['north room 45', 'south room 29'],
	11 : ['room 126', 'room 31', 'room 35'],
	12 : 'north laundry',
	13 : ['babcock room 23', 'blaisdell room 21b', 'carr room 22', 'saunders room 23'],
	14 : 'room 170',
	15 : ['13 story room 52', '5 story room 29'],
	16 : 'room 182',
	17 : ['taft room 13', 'van doren room 13'],
	18 : 'room 1109',
	19 : 'room 100'
}
switcher = {
	1 : [1],
	2 : [2, 3],
	3 : [4],
	4 : [5],
	5 : [6, 7],
	6 : [8, 9],
	7 : [10, 11],
	8 : [12],
	9 : [13, 14],
	10 : [15, 16],
	11 : [17, 18, 19],
	12 : [20],
	13 : [21, 22, 23, 24],
	14 : [25],
	15 : [26, 27],
	16 : [28],
	17 : [29, 30],
	18 : [31],
	19 : [32]
}

Machine = {
	"washer" : 0,
	"dryer" : 1
}

url_laundry_now = "http://classic.laundryview.com/lvs.php?s=1506"

def get_building_id(building_name) :
	return building_id[building_name]

def general_search():
	results = []
	request_url = url_laundry_now
	re_obj = requests.get(request_url)
	bs_obj = BeautifulSoup(re_obj.text.encode("utf8"), "html.parser")
	elements = bs_obj.find("div",{"id" : "campus1"}).findAll("span", {"class" : "user-avail"})
	for key in switcher.keys():
		building = building_id_matcher[key]
		for item in switcher[key]:
			washer_num = int(re.findall(r"\d+", elements[item - 1].get_text())[0])
			dryer_num = int(re.findall(r"\d+", elements[item - 1].get_text())[1])
			results.append({'building' : building, 'room' : item, 'washers' : washer_num, 'dryers' : dryer_num})
	return results

def get_supported_buildings():
	buildings = []
	for key in building_id_matcher:
		buildings.append(building_id_matcher[key])
	return buildings

def get_specific_slots(building_id, machine) : 
	request_url = url_laundry_now
	re_obj = requests.get(request_url)
	bs_obj = BeautifulSoup(re_obj.text.encode("utf8"), "html.parser")
	elements = bs_obj.find("div",{"id" : "campus1"}).findAll("span", {"class" : "user-avail"})
	result = 0
	for index in switcher[building_id] :
		item = re.findall(r"\d+", elements[index].get_text())
		result += int(item[Machine[machine]])
	return result














