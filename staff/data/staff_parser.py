import json

file = open('staff.json', 'r')
staffs = json.load(file)['data']
firstnames = {}
lastnames = {}
middlenames = {}


output = []
for staff in staffs:
	if staff["firstname"].lower() not in firstnames.keys():
		firstnames[staff["firstname"].lower()] = True
		temp = {}
		temp["id"] = staff["firstname"].lower()
		temp["name"] = {}
		temp["name"]["value"] = staff["firstname"]
		output.append(temp)
with open('slot_firstname.json', 'w') as outfile:
    json.dump(output, outfile, sort_keys = True, indent = 4)


output = []
for staff in staffs:
	if staff["lastname"].lower() not in lastnames.keys():
		lastnames[staff["lastname"].lower()] = True
		temp = {}
		temp["id"] = staff["lastname"].lower()
		temp["name"] = {}
		temp["name"]["value"] = staff["lastname"]
		output.append(temp)
with open('slot_lastname.json', 'w') as outfile:
    json.dump(output, outfile, sort_keys = True, indent = 4)


output = []
for staff in staffs:
	if staff["middlename"] == None:
		continue
	if staff["middlename"].lower() not in middlenames.keys():
		middlenames[staff["middlename"].lower()] = True
		temp = {}
		temp["id"] = staff["middlename"].lower()
		temp["name"] = {}
		temp["name"]["value"] = staff["middlename"]
		output.append(temp)
with open('slot_middlename.json', 'w') as outfile:
    json.dump(output, outfile, sort_keys = True, indent = 4)
