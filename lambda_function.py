import logging
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session, request

from search_wirelesschecker import search_wirelesschecker


app = Flask(__name__)
ask = Ask(app, '/')
logging.getLogger("flask_ask").setLevel(logging.DEBUG)


def lambda_handler(event, _context):
    return ask.run_aws_lambda(event)


@ask.launch
def welcome():
    welcome_msg = render_template('welcome')
    return question(welcome_msg)


@ask.intent("AMAZON.HelpIntent")
def help():
    help_msg = render_template('help')
    return question(help_msg)


@ask.intent("AMAZON.FallbackIntent")
def fallback():
    fallback_msg = render_template('error-not-understand')
    return question(fallback_msg)


@ask.intent('AMAZON.CancelIntent')
@ask.intent("AMAZON.StopIntent")
def stop():
    goodbye_msg = render_template('goodbye')
    return statement(goodbye_msg)



@ask.intent('AnswerBuildingNameIntent')
def answer_buildingname(buildingname):
    session.attributes['buildingname'] = buildingname
    confirm_msg = render_template("confirm-clue", 
        which_name="building name", 
        name=buildingname
    )
    return question(confirm_msg)


@ask.intent('StartIntent')
def start_search():

    if 'buildingname' in session.attributes.keys():
        buildingname = session.attributes['buildingname']
    else:
        buildingname = None
    results = search_wirelesschecker(buildingname)
    print(results)

    if len(results) == 0:
        answer_msg = render_template("answer-noresults")
    else:
        answer_msg = render_template("answer-results", result=results[0])
      
    # clear all variables
    #if 'buildingnumber' in session.attributes.keys():
    #    session.attributes.pop('buildingnumber')
    if 'buildingname' in session.attributes.keys():
        session.attributes.pop('buildingname')
    return question(answer_msg)


if __name__ == '__main__':
    app.run(debug=True)
