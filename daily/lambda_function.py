from flask import Flask, render_template
from flask_ask import Ask, request, session, question, statement

from dailynews import DailyNewsSkill

app = Flask(__name__)
ask = Ask(app, "/")

skill = DailyNewsSkill()

def lambda_handler(event, _context):
    return ask.run_aws_lambda(event)


@ask.launch
def launch():
    welcome_text = render_template('welcome')
    help_text = render_template('help')
    session.attributes['lastSpeech'] = welcome_text
    session.attributes['news'] = skill.get_news()
    session.attributes['index'] = 0
    return question(welcome_text).reprompt(help_text)


@ask.intent('DailyNewsInitialIntent')
def initialize_news():
    news = session.attributes['news']
    if len(news) == 0:
        no_news_text = render_template('no_news_problem')
        return question(no_news_text)
    single_news = news[session.attributes['index']]
    news_text = render_template('news', news=single_news)
    help_text = render_template('help')
    session.attributes['lastSpeech'] = news_text
    return question(news_text).reprompt(help_text)


@ask.intent('DailyNewsNextIntent')
def get_next_news():
    news = session.attributes['news']
    session.attributes['index'] += 1
    index = session.attributes['index']
    if index >= len(news):
        exceed_news_text = render_template('exceed_news_problem')
        return question(exceed_news_text)
    single_news = news[index]
    news_text = render_template('news', news=single_news)
    help_text = render_template('help')
    session.attributes['lastSpeech'] = news_text
    return question(news_text).reprompt(help_text)


@ask.intent('DailyNewsPreviousIntent')
def get_previous_news():
    news = session.attributes['news']
    session.attributes['index'] -= 1
    if session.attributes['index'] < 0: session.attributes['index'] = 0
    index = session.attributes['index']
    single_news = news[index]
    news_text = render_template('news', news=single_news)
    help_text = render_template('help')
    session.attributes['lastSpeech'] = news_text
    return question(news_text).reprompt(help_text)


@ask.intent('AMAZON.HelpIntent')
def help():
    help_text = render_template('help')
    session.attributes['lastSpeech'] = help_text
    return question(help_text).reprompt(help_text)


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
    help_text = render_template('help')
    return question(help_text)


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
