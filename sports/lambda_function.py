from flask import Flask, render_template
from flask_ask import Ask, request, session, question, statement

from sports_utils import get_past_games, get_future_games, get_game_by_date, get_supported_list
from sports_consts import sports_list

app = Flask(__name__)
ask = Ask(app, '/')


def lambda_handler(event, _context):
    return ask.run_aws_lambda(event)


@ask.launch
def launch():
    welcome_text = render_template('welcome')
    help_text = render_template('help')
    session.attributes['lastSpeech'] = welcome_text
    session.attributes['sportType'] = None
    return question(welcome_text).reprompt(help_text)


@ask.intent('SportsTypeIntent',
    mapping={'sport': 'sports'},
    default={'sport': 'baseball'})
def get_sport_type(sport):
    if sport not in sports_list:
        error_text = render_template('sport_type_error')
        session.attributes['lastSpeech'] = error_text
        return question(error_text)
    else:
        session.attributes['sportType'] = sport
        help_text = render_template('welcome_sport', sport=sport)
        session.attributes['lastSpeech'] = help_text
        return question(help_text).reprompt(help_text)


@ask.intent('SportsDPastIntent')
def get_past_n_matches(n):
    if n is None:
        n = 1
    n = int(n)
    games = get_past_games(session.attributes['sportType'], n)
    if games is None:
        error_text = render_template('sport_info_error')
        reprompt_text = render_template('reprompt')
        return question(error_text).reprompt(reprompt_text)
    else:
        game_text = render_template('games_info', games=games)
        session.attributes['lastSpeech'] = game_text
        reprompt_text = render_template('reprompt')
        return question(game_text).reprompt(reprompt_text)


@ask.intent('SportsDFutureIntent')
def get_future_n_matches(n):
    if n is None:
        n = 1
    n = int(n)
    games = get_future_games(session.attributes['sportType'], n)
    if games is None:
        error_text = render_template('sport_info_error')
        reprompt_text = render_template('reprompt')
        return question(error_text).reprompt(reprompt_text)
    else:
        game_text = render_template('games_info', games=games)
        session.attributes['lastSpeech'] = game_text
        reprompt_text = render_template('reprompt')
        return question(game_text).reprompt(reprompt_text)


@ask.intent('SportsDDateIntent')
def get_match_by_date(date):
    if date is None:
        error_text = render_template('sport_info_error')
        reprompt_text = render_template('reprompt')
        return question(error_text).reprompt(reprompt_text)
    else:
        games = get_game_by_date(session.attributes['sportType'], date)
        if games is None:
            error_text = render_template('sport_info_error')
            reprompt_text = render_template('reprompt')
            return question(error_text).reprompt(reprompt_text)
        else:
            game_text = render_template('games_info', games=games)
            session.attributes['lastSpeech'] = game_text
            reprompt_text = render_template('reprompt')
            return question(game_text).reprompt(reprompt_text)


@ask.intent('SportSupportedIntent')
def get_supported_sport():
    sports = get_supported_list()
    supported_sports_text = render_template('list_sports', sports=sports)
    session.attributes['lastSpeech'] = supported_sports_text
    reprompt_text = render_template('reprompt')
    return question(supported_sports_text).reprompt(reprompt_text)


@ask.intent('AMAZON.HelpIntent')
def help():
    if session.attributes['sportType'] is not None:
        help_text = render_template('help_sport', sport=session.attributes['sportType'])
    else:
        help_text = render_template('help')
    session.attributes['lastSpeech'] = help_text
    return question(help_text).reprompt(help_text)


@ask.intent('AMAZON.RepeatIntent')
def repeat():
    repeat_text = session.attributes['lastSpeech']
    return question(repeat_text)


@ask.intent('AMAZON.FallbackIntent')
def fallback():
    intent_error_text = render_template('intent_error')
    return question(intent_error_text)


@ask.intent('AMAZON.YesIntent')
def yes():
    if session.attributes['sportType'] is not None:
        help_text = render_template('help_sport', sport=session.attributes['sportType'])
    else:
        help_text = render_template('help')
    session.attributes['lastSpeech'] = help_text
    return question(help_text).reprompt(help_text)


@ask.intent('AMAZON.NoIntent')
def no():
    bye_text = render_template('bye')
    return statement(bye_text)


@ask.intent('AMAZON.StopIntent')
def stop():
    bye_text = render_template('bye')
    return statement(bye_text)


@ask.intent('AMAZON.CancelIntent')
def cancel():
    bye_text = render_template('bye')
    return statement(bye_text)


@ask.session_ended
def session_ended():
    return '{}', 200


if __name__ == '__main__':
    app.run()
