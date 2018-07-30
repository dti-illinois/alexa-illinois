from flask import Flask, render_template
from flask_ask import Ask, request, session, question, statement

from ews import EWSSkill
from ics import ICSSkill
from consts import EWSConsts, ICSConsts

app = Flask(__name__)
ask = Ask(app, "/")

ews_skill = EWSSkill()
ics_skill = ICSSkill()

#deploy as a lambda function
def lambda_handler(event, _context):
    return ask.run_aws_lambda(event)


@ask.launch
def launch():
    welcome_text = render_template('welcome')
    help_text = render_template('help')
    session.attributes['lastSpeech'] = welcome_text
    return question(welcome_text).reprompt(help_text)


@ask.intent('ICSBlurSearchIntent')
def ics_blur_search():
    info = ics_skill.make_blur_search()
    if len(info) == 0:
        blur_search_text = render_template('blur_search_fail')
    else:
        blur_search_text = render_template('ics_blur_search_success', info=info)
    reprompt_text = render_template('reprompt_general')
    session.attributes['lastSpeech'] = blur_search_text
    return question(blur_search_text).reprompt(reprompt_text)


@ask.intent('EWSBlurSearchIntent')
def ews_blur_search():
    info = ews_skill.make_blur_search()
    if len(info) == 0:
        blur_search_text = render_template('blur_search_fail')
    else:
        blur_search_text = render_template('ews_blur_search_success', info=info)
    reprompt_text = render_template('reprompt_general')
    session.attributes['lastSpeech'] = blur_search_text
    return question(blur_search_text).reprompt(reprompt_text)


@ask.intent('BuildingUsageIntent', mapping={'building': 'buildings'}, default={'building': 'digital computer lab'})
def building_usage(building):
    building = building.lower()
    if building in EWSConsts.buildings.keys():
        building = EWSConsts.buildings[building]
        building_info, lab_count, total_free_comp = ews_skill.get_building_info(building)
        building_usage_text = render_template('ews_building_usage_info', building=building, lab_count=lab_count, free_comp_count=total_free_comp, building_info=building_info)
    elif building in ICSConsts.buildings.keys():
        building = ICSConsts.buildings[building]
        building_info = ics_skill.get_building_info(building)
        building_usage_text = render_template('ics_building_usage_info', building=building, building_info=building_info)
    else:
        return question(render_template('building_problem'))
    session.attributes['lastSpeech'] = building_usage_text
    reprompt_text = render_template('reprompt_general')
    return question(building_usage_text).reprompt(reprompt_text)


@ask.intent('EWSRoomUsageIntent', mapping={'building': 'buildings', 'room': 'room_four_digits', 'room_l': 'room_letter', 'room_3': 'room_three_digits'})
def room_usage(building, room, room_l, room_3):
    #shit this is dirty, but I don't know how to make it clean
    if room_l is not None:  room = room_l
    if room_3 is not None:  room = room_3
    building = building.lower()
    room = room.lower()
    if building not in EWSConsts.buildings.keys() or room not in EWSConsts.rooms.keys():
        room_problem_text = render_template('room_problem')
        return question(room_problem_text)
    building = EWSConsts.buildings[building]
    room = EWSConsts.rooms[room]
    room_info = ews_skill.get_room_info(building, room)
    room_usage_text = render_template('room_usage_info', building=EWSConsts.buildings[building],
                                    room=EWSConsts.rooms[room], room_info=room_info)
    session.attributes['lastSpeech'] = room_usage_text
    reprompt_text = render_template('reprompt_general')
    return question(room_usage_text).reprompt(reprompt_text)


@ask.intent('SupportedBuildingsIntent')
def supported_buildings():
    ews_buildings = ews_skill.get_supported_buildings()
    ics_buildings = ics_skill.get_supported_buildings()
    buildings_text = render_template('list_buildings', ews_buildings=ews_buildings, ics_buildings=ics_buildings)
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
