from urllib.request import urlopen
import json

from ews_consts import BUILDINGS, ROOMS

EWS_URL = 'https://my.engr.illinois.edu/labtrack/util_data_json.asp'

#these buildings only have  a limited number of computers
dummy_building_list = ['FAR', 'ESPL', 'PAR', 'REC', 'SDRP']
#buildings that are currently supported
inuse_building_list = ['digital computer lab', 'electrical and computer engineering building',
'engineering hall', 'grainger engineering library', 'mechanical engineering lab',
'siebel center', 'Transportation building']

def get_room_info(building, room):
    building = BUILDINGS[building]
    room = ROOMS[room]
    room_info = _get_ews_usage()[building][room]
    return room_info

def get_supported_buildings():
    buildings = ', '.join(inuse_building_list)
    return buildings

def _get_ews_usage():
    html = urlopen(EWS_URL).read().decode('utf-8')
    data = json.loads(html)['data']
    return _parse_ews_json(data)

def _parse_ews_json(ews_json):
    result = {}
    for item in ews_json:
        [building, room] = (item['strlabname'] + ' dummy').split()[0:2]
        if building == 'GELIB':
            room = '4th floor ' + str(item['strlabname'].split()[-1]).lower()
        #filter out halls with very few computers
        if building in dummy_building_list:
            continue
        building = BUILDINGS[building]
        #create key if it not exist
        if building not in result.keys():
            result[building] = {}
        #fill in the value for the key
        result[building][room] = {
            'inusecount': item['inusecount'],
            'machinecount': item['machinecount']
        }
    return result

print(json.dumps(_get_ews_usage(), indent=4))
print(get_supported_buildings())
