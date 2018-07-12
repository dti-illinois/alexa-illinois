from flask import Flask, render_template
from flask_ask import Ask, request, session, context, question, statement

from cumtd_utils import *

app = Flask(__name__)
ask = Ask(app, '/')

@ask.launch
def launch():
    device_id = context.System.device.deviceId
    session.attributes['stop_name'], session.attributes['stop_id'] = get_stop_info(device_id)
    session.attributes['routes'] = get_routes_on_service(session.attributes['stop_id'])

    welcome_text = render_template('welcome')
    help_text = render_template('help')
    session.attributes['lastSpeech'] = welcome_text
    return question(welcome_text).reprompt(help_text)


@ask.intent('CUMTDStopIntent')
def get_stop():
    stop_name_text = render_template('stop_name', stop_name=session.attributes['stop_name'])
    session.attributes['lastSpeech'] = stop_name_text
    help_text = render_template('help')
    return question(stop_name_text).reprompt(help_text)


@ask.intent('CUMTDRoutesIntent')
def get_routes():
    routes_text = render_template('routes_by_stop', routes=session.attributes['routes'])
    session.attributes['lastSpeech'] = routes_text
    help_text = render_template('help')
    return question(routes_text).reprompt(help_text)


@ask.intent('CUMTDRouteOnServiceIntent')
def get_route_service_by_date(route_id, date):
    help_text = render_template('help')
    if date is None:
        date_error_text = render_template('date_error')
        return question(date_error_text).reprompt(help_text)
    if route_id is not in session.attributes['routes'] or route_id is None:
        route_id_error_text = render_template('route_id_error')
        return question(route_id_error_text).reprompt(help_text)
    on_service = get_route_on_service_by_date(route_id, date)
    route_on_service_by_date_text = render_template('route_on_service_by_date',
    route_id=route_id, on_service=on_service, date=date)
    return question(route_on_service_by_date_text).reprompt(help_text)


@ask.intent('CUMTDRemainingTimeIntent')
def get_remaining_time_by_route(route_id):
    help_text = render_template('help')
    if route_id is None or route_id not in session.attributes['routes']:
        route_id_error_text = render_template('route_id_error')
        return question(route_id_error_text).reprompt(help_text)

    remaining_time_info = get_remaining_time(session.attributes['stop_id'], route_id)
    
    return

@ask.intent('CUMTDSearchRouteIntent')
def get_route_by_destination(destination_stop_name):
    with open('CUMTD_stops_name_key', 'r') as f:
        stops = json.load(f)['stops']
    if destination_stop_id is None or destination_stop_id not in stops.keys():
        pass
    else:
        destination_stop_id = stops[destination_stop_name]
        planned_trip = get_planned_trip(session.attributes['stop_id'], destination_stop_id)


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
