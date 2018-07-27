import json

file = open('wirelesschecker.json', 'r')
studyspaces = json.load(file)['data']
buildingnumbers = {}
buildingnames = {}


'''
output = []
for studyspace in studyspaces:
	if studyspace["buildingnumber"].lower() not in buildingnumbers.keys():
		buildingnumbers[studyspace["buildingnumber"].lower()] = True
		temp = {}
		temp["id"] = studyspace["buildingnumber"].lower()
		temp["name"] = {}
		temp["name"]["value"] = studyspace["buildingnumber"]
		output.append(temp)
with open('slot_buildingnumber.json', 'w') as outfile:
    json.dump(output, outfile, sort_keys = True, indent = 4)
'''

output = []
for studyspace in studyspaces:
	if studyspace["buildingname"].lower() not in buildingnames.keys():
		buildingnames[studyspace["buildingname"].lower()] = True
		temp = {}
		#temp["id"] = studyspace["buildingname"].lower()
		temp["name"] = {}
		temp["name"]["value"] = studyspace["buildingname"]
		output.append(temp)
with open('slot_buildingname.json', 'w') as outfile:
    json.dump(output, outfile, sort_keys = True, indent = 4)


