from urllib.request import urlopen
import json
import datetime

from athletic_consts import AthleticConsts

class AthleticSkill():

    def __init__(self):
        self.base_url = 'https://lyogz55hd1.execute-api.us-west-2.amazonaws.com/api/sports/'

    def get_past_games(self, sport, n):
        data = self._load_data(sport)
        if data is None: return None
        now = datetime.datetime.now().strftime('%Y-%m-%d')
        games = []
        for game in data:
            game = self._reformat(game)
            if game['date'] < now:
                y, m, d = game['date'].split('-')
                game['year'] = y
                game['month'] = AthleticConsts.month_dict[m]
                game['day'] = d
                games.append(game)
        result = sorted(games, key=lambda x: x['date'], reverse=True)[0:n]
        if len(result) == 0:
            return None
        return result

    def get_future_games(self, sport, n):
        data = self._load_data(sport)
        if data is None: return None
        now = datetime.datetime.now().strftime('%Y-%m-%d')
        games = []
        for game in data:
            game = self._reformat(game)
            if game['date'] > now:
                y, m, d = game['date'].split('-')
                game['year'] = y
                game['month'] = AthleticConsts.month_dict[m]
                game['day'] = d
                games.append(game)
        result = sorted(games, key=lambda x: x['date'])[0:n]
        if len(result) == 0:
            return None
        return result

    def get_game_by_date(self, sport, date):
        data = self._load_data(sport)
        if data is None: return None
        result = []
        for game in data:
            game = self._reformat(game)
            if game['date'][4:] == date[4:]:
                y, m, d = game['date'].split('-')
                game['year'] = y
                game['month'] = AthleticConsts.month_dict[m]
                game['day'] = d
                result.append(game)
        if len(result) == 0:
            return None
        return result

    def get_supported_list(self):
        data = self._load_data('list')
        if data is None: return None
        sports_list = []
        for k, v in data.items():
            sports_list.append(v)
        return ', '.join(sports_list)

    def _load_data(self, path):
        try:
            response = urlopen(self.base_url + path)
        except:
            return None
        return json.load(response)

    def _reformat(self, game):
        weekday, date = game['date'].split()
        mon, day, year = date.split('.')
        r_date = datetime.datetime(int('20' + year), int(mon), int(day))
        game['date'] = r_date.strftime('%Y-%m-%d')
        game['time'] = game['time'].replace('CT', 'central time')
        game['time'] = game['time'].replace('TBA', 'to be announced')
        game['result'] = game['result'].replace('W', 'win')
        game['result'] = game['result'].replace('L', 'lose')
        if game['result'] == ' ':
            game['result'] == 'not available'
        return game
