import menu
import logging
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session, request


app = Flask(__name__)
ask = Ask(app, '/')
logging.getLogger("flask_ask").setLevel(logging.DEBUG)


def lambda_handler(event, _context):
    return ask.run_aws_lambda(event)


@ask.launch
def welcome():
    session.attributes['filter'] = {}
    return question(render_template('welcome')) \
        .reprompt(render_template("reprompt"))
    

@ask.intent("AMAZON.HelpIntent")
def help():
    return question(render_template('help'))


@ask.intent("AMAZON.FallbackIntent")
def fallback():
    return question(render_template('error-not-understand'))


@ask.intent('AMAZON.CancelIntent')
@ask.intent("AMAZON.StopIntent")
def stop():
    return statement(render_template('goodbye'))


@ask.intent("DetailIntent")
def detail():
    return menu.detail() \
        .reprompt(render_template("reprompt"))


@ask.intent('FilterIntent')
def add_filter(filter_name):
    return menu.add_filter(filter_name) \
        .reprompt(render_template("reprompt"))


@ask.intent("AskMainIntent", mapping={'hall_name': 'hall'})
def ask_main(hall_name, meal, date):
    return menu.ask_main(hall_name, meal, date) \
        .reprompt(render_template("reprompt"))


@ask.intent("InteractiveIntent")
def interactive():
    return menu.interactive()


@ask.intent("AnswerHallIntent", mapping={'hall_name': 'hall'})
def answer_hall(hall_name):
    return menu.answer_hall(hall_name)


@ask.intent("AnswerMealIntent", mapping={'meal': 'meal'})
def answer_meal(meal):
    return menu.answer_meal(meal)


@ask.intent("AnswerDateIntent", mapping={'date': 'date'})
def answer_date(date):
    return menu.answer_date(date)


if __name__ == '__main__':
    app.run(debug=True)