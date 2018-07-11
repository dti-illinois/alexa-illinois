import json
import data

output = []
catalog = data.get_catalog()
for item in catalog:
	temp = {}
	temp["id"] = item["library_number"]
	temp["name"] = {}
	temp["name"]["value"] = item["unit_name"]
	output.append(temp)

with open('slot_library.json', 'w') as outfile:
    json.dump(output, outfile, sort_keys = True, indent = 4)