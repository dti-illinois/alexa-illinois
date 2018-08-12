import logging
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session, request

from uiuc_laundry import get_building_id
from uiuc_laundry import get_specific_slots
from uiuc_laundry import general_search
from uiuc_laundry import get_supported_buildings

app = Flask(__name__)
ask = Ask(app, '/')
logging.getLogger("flask_ask").setLevel(logging.DEBUG)


def lambda_handler(event, _context):
    return ask.run_aws_lambda(event)

@ask.launch
def welcome():
    welcome_msg = render_template('welcome')
    return question(welcome_msg)

@ask.intent('AMAZON.HelpIntent')
def help():
    help_msg = render_template('help')
    return question(help_msg)

@ask.intent('AMAZON.FallbackIntent')
def fallback():
    fallback_msg = render_template('error-not-understand')
    return question(fallback_msg)

@ask.intent('AMAZON.CancelIntent')
@ask.intent('AMAZON.StopIntent')
def stop():
    goodbye_msg = render_template('goodbye')
    return statement(goodbye_msg)

@ask.intent('InteractiveIntent')
def interactive():
    ask_building_msg = render_template('ask-building')
    return question(ask_building_msg)

@ask.intent('LaundryGeneralSearchIntent')
def general_message():
    info = general_search()
    general_msg = render_template('general_search_answer', info = info)
    help_msg = render_template('reprompt_general')
    return question(general_msg).reprompt(help_msg)

@ask.intent('SupportedBuildingIntent')
def supported_build():
    buildings = get_supported_buildings()
    answer_msg = render_template('answer-supported-building', results = buildings)
    help_msg = render_template('reprompt_general')
    return question(answer_msg).reprompt(help_msg)

@ask.intent("AnswerBuildingIntent", mapping={'building_name': 'building'})
def answer_building(building_name):
    building = request.intent.slots.building.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['id']
    session.attributes['building_id'] = get_building_id(building) 
    session.attributes['building_name'] = building_name

    ask_msg = render_template('ask-machine')

    return question(ask_msg)


@ask.intent("AnswerMachineIntent", mapping={'machine_name': 'machine'})
def answer_machine(machine_name):
    building_id = session.attributes['building_id']
    building_name = session.attributes['building_name']
    machine = request.intent.slots.machine.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['id']
    session.attributes['machine_name'] = machine_name
    results = get_specific_slots(building_id, machine)
    answer_msg = render_template('answer-entress', 
        building=building_name, 
        numbers=results,
        machine=machine
    )
    help_msg = render_template('reprompt_general')
    return question(answer_msg).reprompt(help_msg)

if __name__ == '__main__':
    app.run(debug=True)
