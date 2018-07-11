import json

intents_file = open('intents.json', 'r')
firstname_file = open('data/slot_firstname.json')
lastname_file = open('data/slot_lastname.json')
middlename_file = open('data/slot_middlename.json')

output = json.load(intents_file)
output["interactionModel"]["languageModel"]["types"] = [
	{
		"name": "FIRSTNAME",
		"values": json.load(firstname_file)
	},
	{
		"name": "LASTNAME",
		"values": json.load(lastname_file)
	},
	{
		"name": "MIDDLENAME",
		"values": json.load(middlename_file)
	}
]


with open('model.json', 'w') as outfile:
    json.dump(output, outfile, sort_keys = True, indent = 4)