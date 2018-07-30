from urllib.request import urlopen
import json

from consts import EWSConsts

class EWSSkill():

    def __init__(self):
        self.url = 'https://lyogz55hd1.execute-api.us-west-2.amazonaws.com/api/ews'

    def make_blur_search(self):
        raw = self._load_data()
        result = []
        for building in raw:
            free_comp_count, room = self._get_free_room(raw[building])
            if room is None:    continue
            result.append({'building': building, 'room': room, 'count': free_comp_count})
        result = sorted(result, key=lambda x: x['count'], reverse=True)[0:3]
        return result

    def _get_free_room(self, building_info):
        max_free_comp = 4
        name = None
        for room in building_info:
            tmp = building_info[room]['machinecount'] - building_info[room]['inusecount']
            if tmp > max_free_comp:
                name = room
                max_free_comp = tmp
        return max_free_comp, name

    def get_building_info(self, building):
        raw = self._load_data()[building]
        lab_count, total_free_comp = 0, 0
        for room in raw:
            lab_count += 1
            free_comp = raw[room]['machinecount'] - raw[room]['inusecount']
            raw[room]['free_comp'] = free_comp
            total_free_comp += free_comp
        return raw, lab_count, total_free_comp

    def get_room_info(self, building, room):
        return self._load_data()[building][room]

    def get_supported_buildings(self):
        return ', '.join(EWSConsts.inuse_building_list)

    def _load_data(self):
        data = json.loads(urlopen(self.url).read().decode('utf-8'))
        return self._parse_data(data)

    def _parse_data(self, data):
        result = {}
        for item in data:
            [building, room] = (item['strlabname'] + ' dummy').split()[0:2]
            if building in EWSConsts.dummy_building_list: continue
            if building == 'GELIB': room = 'fourth floor ' + str(item['strlabname'].split()[-1]).lower()
            building = EWSConsts.buildings[building]
            if building not in result.keys():
                result[building] = {}
            result[building][room] = {
                'inusecount': item['inusecount'],
                'machinecount': item['machinecount']
            }
        return result
