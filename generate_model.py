import json

intents_file = open('intents.json', 'r')
buildingname_file = open('data/slot_buildingname.json')
#lastname_file = open('data/slot_lastname.json')


output = json.load(intents_file)
output["interactionModel"]["languageModel"]["types"] = [
	{
		"name": "BUILDINGNAME",
		"values": json.load(buildingname_file)
	}
]


with open('model.json', 'w') as outfile:
    json.dump(output, outfile, sort_keys = True, indent = 4)
