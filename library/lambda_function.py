import logging
import library as lib

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
        .reprompt(render_template('error-not-understand'))


@ask.intent('AMAZON.CancelIntent')
@ask.intent("AMAZON.StopIntent")
def stop():
    return statement(render_template('goodbye'))


@ask.intent('SampleQuestionsIntent')
def sample_questions():
    return question(render_template('sample-questions')) \
        .reprompt(render_template("reprompt"))


@ask.intent('AskCatalogIntent')
def ask_catalog():
    return lib.ask_catalog() \
        .reprompt(render_template("reprompt"))


@ask.intent('AskBasicInfoIntent')
def ask_basic_info(library):
	return lib.ask_basic_info(library) \
        .reprompt(render_template("reprompt"))


@ask.intent('AskNextSevenDaysIntent')
def ask_next_seven_days(library):
    return lib.ask_next_seven_days(library) \
        .reprompt(render_template("reprompt"))


@ask.intent('AskWithDateIntent')
def ask_library_with_date(library, date):
    return lib.ask_with_date(library, date) \
        .reprompt(render_template("reprompt"))


if __name__ == '__main__':
    app.run(debug=True)