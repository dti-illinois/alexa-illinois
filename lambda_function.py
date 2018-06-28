import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session, request

from dining import get_hall_id
from dining import get_dining_today

app = Flask(__name__)
ask = Ask(app, '/')
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

def lambda_handler(event, _context):
    return ask.run_aws_lambda(event)

@ask.launch
def ask_hall():
    ask_hall_msg = render_template('ask-hall')
    return question(ask_hall_msg)

@ask.intent("AnswerHallIntent", mapping={'hall_name': 'hall'})
def ask_meal(hall_name):
    hall = request.intent.slots.hall.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['id']
    
    session.attributes['hall_id'] = get_hall_id(hall) # reverse
    session.attributes['hall_name'] = hall_name
    ask_meal_msg = render_template('ask-meal', hall=hall_name)
    return question(ask_meal_msg)

@ask.intent("AnswerMealIntent", mapping={'meal_name': 'meal'})
def answer(meal_name):
    hall_id = session.attributes['hall_id']
    hall_name = session.attributes['hall_name']
    meal = request.intent.slots.meal.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['id']

    print(meal)
    results = get_dining_today(hall_id, meal, 'Entrees')
    answer_msg = render_template('answer-entrees', 
        hall=hall_name, 
        meal=meal_name, 
        results=results
    )
    return statement(answer_msg)

if __name__ == '__main__':
    app.run(debug=True)