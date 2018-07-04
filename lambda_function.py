from flask import Flask, render_template
from flask_ask import Ask, request, session, question, statement

from ews_utils import get_building_info, get_room_info, get_supported_buildings

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


@ask.intent('EWSBlurSearchIntent')
def blur_search():
    pass


@ask.intent('EWSBuildingUsageIntent',
    mapping={'building': 'buildings'},
    default={'building': 'digital computer lab'})
def building_usage(building):
    building_info, lab_count, total_free_comp = get_building_info(building)
    building_usage_text = render_template('building_usage_info', building=building,
                                        lab_count=lab_count, free_comp_count=total_free_comp,
                                        building_info=building_info)
    reprompt_text = render_template('reprompt_general')
    return question(building_usage_text).reprompt(reprompt_text)


@ask.intent('EWSRoomUsageIntent',
    mapping={'building': 'buildings', 'room': 'rooms'},
    default={'building': 'digital computer lab', 'room': 'L416'})
def room_usage(building, room):
    room_info = get_room_info(building, room)
    room_usage_text = render_template('room_usage_info', building=building,
                                    room=room, room_info=room_info)
    reprompt_text = render_template('reprompt_general')
    return question(room_usage_text).reprompt(reprompt_text)


@ask.intent('EWSSupportedBuildingsIntent')
def supported_buildings():
    buildings = get_supported_buildings()
    buildings_text = render_template('list_buildings', buildings=buidlings)
    reprompt_text = render_template('reprompt_general')
    return question(buildings_text).reprompt(reprompt_text)


@ask.intent('AMAZON.HelpIntent')
def help():
    help_text = render_template('help')
    reprompt_text = render_template('reprompt_help')
    return question(help_text).reprompt(reprompt_text)


@ask.intent('AMAZON.YesIntent')
def yes():
    question_text = render_template('reprompt_help')
    return question(question_text).reprompt(question_text)


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
    return "{}", 200

if __name__ == '__main__':
    app.run()
