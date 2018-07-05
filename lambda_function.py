import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session, request

from dining import get_hall_id
from dining import get_dining_today
from dining import get_dining_tomorrow

app = Flask(__name__)
ask = Ask(app, '/')
logging.getLogger("flask_ask").setLevel(logging.DEBUG)


def lambda_handler(event, _context):
    return ask.run_aws_lambda(event)


def answer_entrees():
    hall_id = session.attributes['hall_id']
    hall_name = session.attributes['hall_name']
    meal = session.attributes['meal']
    date = session.attributes['date']
    if date == 'today':
        results = get_dining_today(hall_id, meal, 'Entrees')
    elif date == 'tomorrow':
        results = get_dining_tomorrow(hall_id, meal, 'Entrees')
    else:
        pass
    if not results == None:
        answer_msg = render_template('answer-entrees-ask', 
            hall=hall_name, meal=meal, date=date,
            results=results
        )
    else:
        answer_msg = render_template('error-not-found')
    return question(answer_msg)


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


@ask.intent("InteractiveIntent")
def interactive():
    ask_hall_msg = render_template('inter-ask-hall')
    return question(ask_hall_msg)


@ask.intent("AnswerHallIntent", mapping={'hall_name': 'hall'})
def answer_hall(hall_name):
    # get hall id from request
    hall = request.intent.slots.hall.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['id']
    # store hall id and name into session
    session.attributes['hall_id'] = get_hall_id(hall) 
    session.attributes['hall_name'] = hall_name
    # ask other not answered specs
    if 'hall_name' not in session.attributes.keys():
        ask_msg = render_template('inter-ask-hall')
    elif 'meal' not in session.attributes.keys():
        ask_msg = render_template('inter-ask-meal')
    elif 'date' not in session.attributes.keys():
        ask_msg = render_template('inter-ask-date')
    else:
        return answer_entrees()
    return question(ask_msg)


@ask.intent("AnswerMealIntent", mapping={'meal': 'meal'})
def answer_meal(meal):
    # get meal name from request
    meal = request.intent.slots.meal.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['id']
    # store meal into session
    session.attributes['meal'] = meal
    # ask other not answered specs
    if 'hall_name' not in session.attributes.keys():
        ask_msg = render_template('inter-ask-hall')
    elif 'meal' not in session.attributes.keys():
        ask_msg = render_template('inter-ask-meal')
    elif 'date' not in session.attributes.keys():
        ask_msg = render_template('inter-ask-date')
    else:
        return answer_entrees()
    return question(ask_msg)


@ask.intent("AnswerDateIntent", mapping={'date': 'date'})
def answer_date(date):
    # get date (today or tomorrow) from request
    date = request.intent.slots.date.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['id']
    # store date into session
    session.attributes['date'] = date
    # ask other not answered specs
    if 'hall_name' not in session.attributes.keys():
        ask_msg = render_template('inter-ask-hall')
    elif 'meal' not in session.attributes.keys():
        ask_msg = render_template('inter-ask-meal')
    elif 'date' not in session.attributes.keys():
        ask_msg = render_template('inter-ask-date')
    else:
        return answer_entrees()
    return question(ask_msg)


@ask.intent("AskMainIntent", mapping={'hall_name': 'hall', 'meal': 'meal', 'date': 'date'})
def ask_main(hall_name, meal, date):
    # get all info from request
    hall = request.intent.slots.hall.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['id']
    meal = request.intent.slots.meal.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['id']
    date = request.intent.slots.date.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['id']
    # store them in the session
    session.attributes['hall_id'] = get_hall_id(hall) 
    session.attributes['hall_name'] = hall_name
    session.attributes['meal'] = meal
    session.attributes['date'] = date
    print(date)
    return answer_entrees()


if __name__ == '__main__':
    app.run(debug=True)