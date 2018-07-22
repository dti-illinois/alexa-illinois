from flask import Flask, render_template
from flask_ask import Ask, request, session, context, question, statement

from cumtd_utils import *

app = Flask(__name__)
ask = Ask(app, '/')

with open('data/CUMTD_stops_name_key.json', 'r') as f:
    stops = json.load(f)['stops']

#deploy as a lambda function
def lambda_handler(event, _context):
    return ask.run_aws_lambda(event)
    
@ask.launch
def launch():
    device_id = context.System.device.deviceId
    session.attributes['stop_name'], session.attributes['stop_id'] = get_stop_info(device_id)
    session.attributes['routes'] = get_routes_on_service(session.attributes['stop_id'])
    session.attributes['remainingTrips'] = []

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
    route_id = route_id.upper()
    if date is None:
        date_error_text = render_template('date_error')
        return question(date_error_text).reprompt(help_text)
    if route_id not in session.attributes['routes'] or route_id is None:
        route_id_error_text = render_template('route_id_error')
        return question(route_id_error_text).reprompt(help_text)
    on_service = get_route_on_service_by_date(route_id, date)
    route_on_service_by_date_text = render_template('route_on_service_by_date',
    route_id=route_id, on_service=on_service, date=date)
    session.attributes['lastSpeech'] = route_on_service_by_date_text
    return question(route_on_service_by_date_text).reprompt(help_text)


@ask.intent('CUMTDRemainingTimeIntent')
def get_remaining_time_by_route(route_id):
    help_text = render_template('help')
    route_id = route_id.upper()
    if route_id is None or route_id not in session.attributes['routes']:
        route_id_error_text = render_template('route_id_error')
        return question(route_id_error_text).reprompt(help_text)

    remaining_time_info = get_remaining_time(session.attributes['stop_id'], route_id)
    if remaining_time_info == []:
        no_bus_comming_error_text = render_template('no_bus_comming_error', route=route_id)
        return question(no_bus_comming_error_text).reprompt(help_text)

    remaining_time_by_route_text = render_template('remaining_time_by_route', info=remaining_time_info[0])
    session.attributes['lastSpeech'] = remaining_time_by_route_text
    return question(remaining_time_by_route_text).reprompt(help_text)

@ask.intent('CUMTDSearchRouteIntent')
def get_route_by_destination(destination_stop_name):
    help_text = render_template('help')
    destination_stop_name = destination_stop_name.replace('and', '&').lower()
    if destination_stop_name is None or destination_stop_name not in stops.keys():
        stop_name_error_text = render_template('stop_name_error')
        return question(stop_name_error_text).reprompt(help_text)
    else:
        destination_stop_id = stops[destination_stop_name]
        planned_trips = get_planned_trip(session.attributes['stop_id'], destination_stop_id)
        if len(planned_trips) == 0:
            trip_error_text = render_template('trip_error')
            return question(trip_error_text).reprompt(help_text)
        session.attributes['remainingTrips'] = planned_trips[1:]
        planned_trip_text = render_template('planned_trip', info=planned_trips[0])
        return question(planned_trip_text).reprompt(help_text)


@ask.intent('CUMTDChangeIntent')
def change():
    help_text = render_template('help')
    if len(session.attributes['remainingTrips']) == 0:
        trip_error_text = render_template('trip_error')
        return question(trip_error_text).reprompt(help_text)
    planned_trip_text = render_template('planned_trip', info=session.attributes['remainingTrips'][0])
    session.attributes['remainingTrips'] = session.attributes['remainingTrips'][1:]
    return question(planned_trip_text).reprompt(help_text)


@ask.intent('AMAZON.HelpIntent')
def help():
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
    help_text = render_template('help')
    return question(help_text)


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
