import json
import datetime
import urllib.request
from bs4 import BeautifulSoup

from sports_consts import SPORTS

BASE_URL = 'http://www.fightingillini.com/schedule.aspx?path='
PATH = 'sports.json'

def print_to_file(path):
    data = {}
    for sport in SPORTS.keys():
        print(sport)
        data[SPORTS[sport]] = get_sport_info(sport)
    with open(path, 'w') as f:
        json.dump({'data':data}, f, indent=4)

def get_sport_info(sport):
    sport = sport.lower()
    if sport in SPORTS.keys():
        request_url = BASE_URL + sport
        req = urllib.request.Request(request_url, None,
        {'User-agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'})
        response = urllib.request.urlopen(req)
        soup = BeautifulSoup(response, 'html.parser')
        games = []
        for item in soup.find_all(class_='schedule_game'):
            game = {}
            game['opponent'] = _get_opponent(item)
            game['date'] = _get_date(item)
            game['time'] = _get_time(item)
            game['location'] = _get_location(item)
            game['result'] = _get_result(item)
            try:
                game = _reformat(game)
            except:
                continue
            games.append(game)
        return games
    else:
        return None

def _reformat(j):
    weekday, date = j['date'].split()
    mon, day, year = date.split('.')
    r_date = datetime.datetime(int('20' + year), int(mon), int(day))
    j['date'] = r_date.strftime('%Y-%m-%d')
    j['time'] = j['time'].replace('CT', 'central time')
    j['time'] = j['time'].replace('TBA', 'to be announced')
    j['result'] = j['result'].replace('W', 'win')
    j['result'] = j['result'].replace('L', 'lose')
    if j['result'] == ' ':
        j['result'] == 'not available'
    return j

def _get_opponent(game):
    opponent_div = game.find(class_='schedule_game_opponent_name')
    if opponent_div.a is None and opponent_div.span is None:
        return opponent_div.string.strip()
    elif opponent_div.span is None:
        if opponent_div.a.string is None:
            return opponent_div.a.span.string.strip()
        else:
            return opponent_div.a.string.strip()
    else:
        return opponent_div.span.string.strip()

def _get_date(game):
    date_div = game.find(class_='schedule_game_opponent_date')
    return date_div.string.strip()

def _get_time(game):
    time_div = game.find(class_='schedule_game_opponent_time')
    return time_div.string.strip()

def _get_location(game):
    location_div = game.find(class_='schedule_game_location')
    if location_div.span is None:
        return location_div.string.strip()
    else:
        if location_div.span.string is None:
            return 'not available'
        else:
            return location_div.span.string.strip()

def _get_result(game):
    result_div = game.find(class_='schedule_game_results')
    if result_div is None or len(result_div.div.contents) == 0:
        return 'not available'
    else:
        return result_div.div.contents[0]

print_to_file(PATH)
