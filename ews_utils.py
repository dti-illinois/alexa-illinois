from urllib.request import urlopen
import json

from ews_consts import BUILDINGS, ROOMS

EWS_URL = 'https://my.engr.illinois.edu/labtrack/util_data_json.asp'


def get_room_info(building, room):
    building = BUILDINGS[building]
    room = ROOMS[room]
    room_info = _get_ews_usage()[building][room]
    statement_text = render_template('room_usage_info', building=building,
                                    room=room, room_info=room_info)
    return question(statement_text)

def _get_ews_usage():
    html = urlopen(EWS_URL).read().decode('utf-8')
    data = json.loads(html)['data']
    return _parse_ews_json(data)

def _parse_ews_json(ews_json):
    result = {}
    for item in ews_json:
        [building, room] = (item['strlabname'] + ' dummy').split()[0:2]
        building = BUILDINGS[building]
        #filter out halls with very few computers
        if building == 'FAR' or building == 'ESPL'
        or building == 'PAR' or building == 'REC'
        or building == 'SDRP':
            continue
        #create key if it not exist
        if building not in result.keys():
            result[building] = {}
        #fill in the value for the key
        result[building][room] = {
            'inusecount': item['inusecount'],
            'machinecount': item['machinecount']
        }
    return result
