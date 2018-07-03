from flask import Flask, render_template
from flask_ask import Ask, request, session, question, statement

from ews_utils import get_room_info

app = Flask(__name__)
ask = Ask(app, "/")

#deploy as a lambda function
def lambda_handler(event, _context):
    return ask.run_aws_lambda(event)


@ask.launch
def launch():
    welcome_text = render_template('welcome')
    help_text = render_template('help')
    return question(welcome_text).reprompt(help_text)


@ask.intent('EWSRoomUsageIntent',
    mapping={'building': 'buildings', 'room': 'rooms'},
    default={'building': 'digital computer lab', 'room': 'L416'})
def get_room_usage(building, room):
    room_info = get_room_info(building, room)
    statement_text = render_template('room_usage_info', building=building,
                                    room=room, room_info=room_info)
    reprompt_text = render_template('reprompt_general')
    return question(statement_text).reprompt(reprompt_text)


@ask.intent('EWSSupported')


@ask.intent('AMAZON.HelpIntent')
def help():
    help_text = render_template('help')
    reprompt_text = render_template('reprompt_help')
    return question(help_text).reprompt(reprompt_text)


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

if __name__ == '__main__':
    app.run()
