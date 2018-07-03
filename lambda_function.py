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


@ask.intent('OneshotEWSIntent',
    mapping={'building': 'buildings', 'room': 'rooms'},
    default={'building': 'digital computer lab', 'room': 'L416'})
def one_shot_ews_usage(building, room):
    return get_room_info(building, room)


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
