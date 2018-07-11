from flask import Flask, render_template
from flask_ask import Ask, request, session, context, question, statement

from cumtd_utils import *

app = Flask(__name__)
ask = Ask(app, '/')

@ask.launch
def launch():
    device_id = context.System.device.deviceId
    session.attributes['deviceId'] = device_id
    welcome_text = render_template('welcome')
    help_text = render_template('help')
    session.attributes['lastSpeech'] = welcome_text
    return question(welcome_text).reprompt(help_text)


@ask.intent('CUMTDStopIntent')
def get_stop():
    stop_name = get_stop_name(session.attributes['deviceId'])
    stop_name_text = render_template('stop_name', stop_name=stop_name)
    session.attributes['lastSpeech'] = stop_name_text
    help_text = render_template('help')
    return question(stop_name_text).reprompt(help_text)


@ask.intent('CUMTDRoutesIntent')
def get_routes():
    routes = get_routes_by_stop(session.attributes['deviceId'])
    routes_text = render_template('routes_by_stop', routes=routes)
    session.attributes['lastSpeech'] = routes_text
    help_text = render_template('help')
    return question(routes_text).reprompt(help_text)


@ask.intent('CUMTDRouteOnServiceIntent')
def get_route_on_service():
    pass


@ask.intent('CUMTDRemainingTimeIntent')
def get_remaining_time_by_route():
    pass


@ask.intent('CUMTDSearchRouteIntent')
def get_route_by_detination():
    pass


@ask.intent('AMAZON.HelpIntent')
def help():
    pass


@ask.intent('AMAZON.RepeatIntent')
def repeat():
    repeat_text = session.attributes['lastSpeech']
    return question(repeat_text)


@ask.intent('AMAZON.FallbackIntent')
def fallback():
    intent_error_text = render_template('intent_error')
    return qeustion(intent_error_text)


@ask.intent('AMAZON.YesIntent')
def yes():
    pass


@ask.intent('AMAZON.NoIntent')
def no():
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
