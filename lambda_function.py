from flask import Flask, render_template
from flask_ask import Ask, request, session, question, statement

import json

from consts import BUILDINGS, ROOMS
from ews_usage import get_ews_usage


app = Flask(__name__)
ask = Ask(app, "/")


def lambda_handler(event, _context):
    return ask.run_aws_lambda(event)


@ask.launch
def launch():
    welcome_text = render_template('welcome')
    help_text = render_template('help')
    return question(welcome_text).reprompt(help_text)


@ask.intent('OneshotEWSIntent',
    mapping={'building': 'buildings', 'room': 'rooms'},
    default={'building': 'digital computer lab', 'room': 'L416'})
def one_shot_ews_usage(building, room):
    building = BUILDINGS[building]
    room = ROOMS[room]
    return _get_room_info(building, room)


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
    return "{}", 200


def _get_room_info(building, room):
    room_info = _parse_ews_json(get_ews_usage())[building][room]
    statement_text = render_template('room_usage_info', building=building,
                                    room=room, room_info=room_info)
    return statement(statement_text)

def _parse_ews_json(ews_json):
    result = {}
    for item in ews_json:
        [building, room] = (item['strlabname'] + ' dummy').split()[0:2]
        building = BUILDINGS[building]
        if building not in result.keys():
            result[building] = {}
        result[building][room] = {
            'inusecount': item['inusecount'],
            'machinecount': item['machinecount']
        }
    return result


#if __name__ == '__main__':
    #app.run()
    #print(json.dumps(_parse_ews_json(get_ews_usage()), indent=4))
