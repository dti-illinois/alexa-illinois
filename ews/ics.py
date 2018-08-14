from urllib.request import urlopen
import json

from consts import ICSConsts

class ICSSkill():

    def __init__(self):
        self.url = 'https://69smoo2dc6.execute-api.us-east-1.amazonaws.com/api/ics'

    def make_blur_search(self):
        raw = self._load_data()
        result = []
        for building in raw:
            free_comp_count = raw[building]['machinecount'] - raw[building]['inusecount']
            result.append({'building': building, 'count': free_comp_count})
        result = sorted(result, key=lambda x: x['count'], reverse=True)[0:3]
        if result[0]['count'] < 5:  return []
        return result

    def get_building_info(self, building):
        return self._load_data()[building]

    def get_supported_buildings(self):
        return ', '.join(ICSConsts.inuse_building_list)

    def _load_data(self):
        data = json.loads(urlopen(self.url).read().decode('utf-8'))
        return self._parse_data(data)

    def _parse_data(self, data):
        result = {}
        for item in data:
            if item['site_name'] in ICSConsts.dummy_building_list: continue
            building = ICSConsts.buildings[item['site_name'].lower()]
            result[building] = {
                'inusecount': item['usage_active'],
                'machinecount': item['usage_total']
            }
        return result
