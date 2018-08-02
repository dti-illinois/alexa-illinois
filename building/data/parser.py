import json
import csv

# table building and info as input
buildings = json.load(open("original.json", 'r'))["building"]
table = []
with open('IlliniBldg.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        row[0] = int(row[0])
        table.append(row)

# convert buildings
for i in range(1, len(buildings)):
    if buildings[i]['BLDG_NUM'] != '':
        buildings[i]['BLDG_NUM'] = int(buildings[i]['BLDG_NUM'])
    else:
        if buildings[i-1][0]['BLDG_NUM'] == '':
            buildings[i-2].append(buildings[i])
        else: 
            buildings[i-1].append(buildings[i])
    buildings[i] = [buildings[i]]

output = []
for i in range(1, len(buildings)):
    if buildings[i][0]['BLDG_NUM'] != '':
        output.append(buildings[i])

for i in range(len(output)):
    bldg_num = output[i][0]['BLDG_NUM']
    for j in range(len(table)):
        if bldg_num == table[j][0]:
            output[i][0]['FULL_NAME'] = table[j][1]
            output[i][0]['STREET_ADDR'] = table[j][2]
            output[i][0]['FULL_ADDR'] = table[j][6]
            output[i][0]['LAT'] = table[j][7]
            output[i][0]['LONG'] = table[j][8]

with open('buildings.json', 'w') as outfile:
    json.dump(output, outfile, sort_keys = True, indent = 4)
