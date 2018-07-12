import json

file = open('buildings.json', 'r')
buildings = json.load(file)['data']


output = []
for building in buildlings:
	temp = {}
	temp["id"] = building["number"]
	temp["name"] = {}
	temp["name"]["value"] = building["name"]
	output.append(temp)