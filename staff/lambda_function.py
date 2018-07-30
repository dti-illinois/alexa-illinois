import staff
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
    return question(render_template('welcome')) \
        .reprompt(render_template("reprompt"))


@ask.intent("AMAZON.HelpIntent")
def help():
    return question(render_template('help')) \
        .reprompt(render_template("reprompt"))


@ask.intent("AMAZON.FallbackIntent")
def fallback():
    return question(render_template('error-not-understand')) \
        .reprompt(render_template("error-not-understand"))


@ask.intent('AMAZON.CancelIntent')
@ask.intent("AMAZON.StopIntent")
def stop():
    return statement(render_template('goodbye'))


@ask.intent('AnswerFirstNameIntent')
def answer_firstname(firstname):
    return staff.answer_firstname(firstname)


@ask.intent('AnswerLastNameIntent')
def answer_lastname(lastname):
    return staff.answer_lastname(firstname)


@ask.intent('AnswerMiddleNameIntent')
def answer_middlename(middlename):
    return staff.answer_middlename(firstname)


@ask.intent('StartIntent')
def start_search():
    return staff.start_search()


if __name__ == '__main__':
    app.run(debug=True)