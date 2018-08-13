from urllib.request import urlopen
import json
import re

from consts import DailyNewsConsts

class DailyNewsSkill():

    def __init__(self):
        self.url = 'https://hs7k17eh68.execute-api.us-west-2.amazonaws.com/api/dailynews'

    def get_news(self):
        data = self._load_data()
        print(json.dumps(data, indent=4))
        return data

    def _load_data(self):
        data = json.loads(urlopen(self.url).read().decode('utf-8'))
        return self._parse_data(data)

    def _parse_data(self, data):
        for item in data:
            item['date'] = DailyNewsConsts.weekday[item['date'].split(',')[0]]
            item['description'] = self._reformat_description(item['description'])
        return data

    def _reformat_description(self, description):
        description = description.replace(u'\xa0', u' ')
        reversed = description[::-1][3:]
        reversed = re.split(r' ,| \.', reversed)[1:]
        return ' .'.join(reversed)[::-1]
