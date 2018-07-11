import json
import datetime

from sports_consts import sports_list

PATH = 'sports.json'
Mon = {
'01': 'January',
'02': 'February',
'03': 'March',
'04': 'April',
'05': 'May',
'06': 'June',
'07': 'July',
'08': 'August',
'09': 'September',
'10': 'October',
'11': 'November',
'12': 'December'
}
def get_past_games(sport, n):
    data = _get_sport_data(sport)
    now = datetime.datetime.now().strftime('%Y-%m-%d')
    games = []
    for game in data:
        if game['date'] < now:
            y, m, d = game['date'].split('-')
            game['year'] = y
            game['month'] = Mon[m]
            game['day'] = d
            games.append(game)
    result = sorted(games, key=lambda x: x['date'], reverse=True)[0:n]
    if len(result) == 0:
        return None
    else:
        return result

def get_future_games(sport, n):
    data = _get_sport_data(sport)
    now = datetime.datetime.now().strftime('%Y-%m-%d')
    games = []
    for game in data:
        if game['date'] > now:
            y, m, d = game['date'].split('-')
            game['year'] = y
            game['month'] = Mon[m]
            game['day'] = d
            games.append(game)
    result = sorted(games, key=lambda x: x['date'])[0:n]
    if len(result) == 0:
        return None
    else:
        return result

def get_game_by_date(sport, date):
    data = _get_sport_data(sport)
    result = []
    for game in data:
        if game['date'][4:] == date[4:]:
            y, m, d = game['date'].split('-')
            game['year'] = y
            game['month'] = Mon[m]
            game['day'] = d
            result.append(game)
    if len(result) == 0:
        return None
    else:
        return result

def get_supported_list():
    sports = ', '.join(sports_list)
    return sports

def _get_sport_data(sport):
    with open(PATH, 'r') as f:
        data = json.load(f)
    return data['data'][sport]
