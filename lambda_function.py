from flask import Flask, render_template
from flask_ask import Ask, request, session, question, statement

from ews_utils import make_blur_search, get_building_info, get_room_info, get_supported_buildings
from ews_utils import BUILDINGS, ROOMS
app = Flask(__name__)
ask = Ask(app, "/")

#deploy as a lambda function
def lambda_handler(event, _context):
    return ask.run_aws_lambda(event)


@ask.launch
def launch():
    welcome_text = render_template('welcome')
    help_text = render_template('help')
    session.attributes['lastSpeech'] = welcome_text
    return question(welcome_text).reprompt(help_text)


@ask.intent('EWSBlurSearchIntent')
def blur_search():
    info = make_blur_search()
    if len(info) == 0:
        blur_search_text = render_template('blur_search_fail')
    else:
        blur_search_text = render_template('blue_search_success', info=info)
    reprompt_text = render_template('reprompt_general')
    session.attributes['lastSpeech'] = blur_search_text
    return question(blur_search_text).reprompt(reprompt_text)


@ask.intent('EWSBuildingUsageIntent',
    mapping={'building': 'buildings'},
    default={'building': 'digital computer lab'})
def building_usage(building):
    building_info, lab_count, total_free_comp = get_building_info(building)
    if building_info is None:
        building_problem_text = render_template('building_problem')
        return question(building_problem_text)
    building_usage_text = render_template('building_usage_info', building=BUILDINGS[building],
                                        lab_count=lab_count, free_comp_count=total_free_comp,
                                        building_info=building_info)
    session.attributes['lastSpeech'] = building_usage_text
    reprompt_text = render_template('reprompt_general')
    return question(building_usage_text).reprompt(reprompt_text)


@ask.intent('EWSRoomUsageIntent',
    mapping={'building': 'buildings', 'room': 'room_four_digits', 'room_l': 'room_letter', 'room_3': 'room_three_digits'})
def room_usage(building, room, room_l, room_3):
    #shit this is dirty, but I don't know how to make it clean
    if room_l is not None:  room = room_l
    if room_3 is not None:  room = room_3

    room_info = get_room_info(building, room)
    if room_info is None:
        room_problem_text = render_template('room_problem')
        return question(room_problem_text)
    room_usage_text = render_template('room_usage_info', building=BUILDINGS[building],
                                    room=ROOMS[room], room_info=room_info)
    session.attributes['lastSpeech'] = room_usage_text
    reprompt_text = render_template('reprompt_general')
    return question(room_usage_text).reprompt(reprompt_text)


@ask.intent('EWSSupportedBuildingsIntent')
def supported_buildings():
    buildings = get_supported_buildings()
    buildings_text = render_template('list_buildings', buildings=buildings)
    session.attributes['lastSpeech'] = buildings_text
    reprompt_text = render_template('reprompt_general')
    return question(buildings_text).reprompt(reprompt_text)


@ask.intent('AMAZON.HelpIntent')
def help():
    help_text = render_template('help')
    reprompt_text = render_template('reprompt_help')
    session.attributes['lastSpeech'] = help_text
    return question(help_text).reprompt(reprompt_text)

@ask.intent('AMAZON.RepeatIntent')
def repeat():
    repeat_text = session.attributes['lastSpeech']
    return question(repeat_text)

@ask.intent('AMAZON.FallbackIntent')
def fallback():
    intent_problem_text = render_template('intent_problem')
    return question(intent_problem_text)

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
