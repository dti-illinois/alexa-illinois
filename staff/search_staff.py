import json

def search_staff(firstname, lastname, middlename):
	file = open('data/staff.json', 'r')
	staffs = json.load(file)['data']

	results = []
	for staff in staffs:
		if firstname  != None and firstname  != staff['firstname'].lower():  continue
		if lastname   != None and lastname   != staff['lastname'].lower():   continue
		if middlename != None and middlename != staff['middlename'].lower(): continue
		results.append(staff)
	return results