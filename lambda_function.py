from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

from dining import get_dining_today

app = Flask(__name__)
ask = Ask(app, '/')


def lambda_handler(event, context):
    return ask.run_aws_lambda(event)


@ask.launch
def ask_hall():
    ask_hall_msg = render_template('ask-hall')
    return question(ask_loc_msg)


@ask.intent("AnswerHallIntent", convert={'hall': str})
def ask_meal(hall):
    ask_meal_msg = render_template('ask-meal', hall=hall)
    session.attributes['hall_id'] = get_hall_id(hall) # reverse
    return question(ask_meal)


@ask.intent("AnswerMealIntent", meal={'meal': str})
def answer(meal):
    hall_id = session.attributes['hall_id']
    results = get_dining_today(hall_id, meal, 'Entrees')
    render_template('answer-entrees', 
        hall=hall_id, 
        meal=meal, 
        results=results
    )
    return statement(msg)