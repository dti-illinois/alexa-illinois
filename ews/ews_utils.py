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

def make_blur_search():
    result = []
    raw = _get_ews_usage()
    for building in raw:
        free_comp_count, room = _get_free_room(raw[building])
        if room is None:
            continue
        result.append({'building': building,
                        'room': room,
                        'count': free_comp_count})
    return sorted(result, key=lambda x: x['count'], reverse=True)[0:3]

def get_building_info(building):
    if building not in BUILDINGS.keys():
        return None, None, None
    building = BUILDINGS[building]
    raw = _get_ews_usage()[building]
    lab_count, total_free_comp = 0, 0
    for room in raw:
        lab_count += 1
        free_comp = raw[room]['machinecount'] - raw[room]['inusecount']
        raw[room]['free_comp'] = free_comp
        total_free_comp += free_comp
    return raw, lab_count, total_free_comp

def get_room_info(building, room):
    print(building)
    print(room)
    if building not in BUILDINGS.keys() or room not in ROOMS.keys():
        return None
    building = BUILDINGS[building]
    room = ROOMS[room]
    room_info = _get_ews_usage()[building][room]
    return room_info

def get_supported_buildings():
    buildings = ', '.join(inuse_building_list)
    return buildings

def _get_free_room(building_info):
    max_free_comp = 4
    name = None
    for room in building_info:
        tmp = building_info[room]['machinecount'] - building_info[room]['inusecount']
        if tmp > max_free_comp:
            name = room
            max_free_comp = tmp
    return max_free_comp, name

def _get_ews_usage():
    html = urlopen(EWS_URL).read().decode('utf-8')
    data = json.loads(html)['data']
    return _parse_ews_json(data)

def _parse_ews_json(ews_json):
    result = {}
    for item in ews_json:
        [building, room] = (item['strlabname'] + ' dummy').split()[0:2]
        if building == 'GELIB':
            room = 'fourth floor ' + str(item['strlabname'].split()[-1]).lower()
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

#print(json.dumps(_get_ews_usage(), indent=4))
#print(get_supported_buildings())
#a, b, c =get_building_info('digital computer lab')
#print(json.dumps(a, indent=4))
#print(make_blur_search())
