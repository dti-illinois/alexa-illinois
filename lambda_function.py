from flask import Flask, render_template
from flask_ask import Ask, request, session, context, question, statement

app = Flask(__name__)
ask = Ask(app, '/')

@ask.launch
def launch():
    pass


@ask.intent('CUMTDStopIntent')
def get_stop():
    pass


@ask.intent('CUMTDRoutesIntent')
def get_routes():
    pass


@ask.intent('CUMTDRouteOnServiceIntent')
def get_route_on_service():
    pass


@ask.intent('CUMTDRemainingTimeIntent')
def get_remaining_time_by_route():
    pass


@ask.intent('CUMTDSearchRouteIntent')
def get_route_by_detination():
    pass


@ask.intent('AMAZON.HelpIntent')
def help():
    pass


@ask.intent('AMAZON.RepeatIntent')
def repeat():
    repeat_text = session.attributes['lastSpeech']
    return question(repeat_text)


@ask.intent('AMAZON.FallbackIntent')
def fallback():
    intent_error_text = render_template('intent_error')
    return qeustion(intent_error_text)


@ask.intent('AMAZON.YesIntent')
def yes():
    pass


@ask.intent('AMAZON.NoIntent')
def no():
    bye_text = render_template('bye')
    return statement(bye_text)


@ask.intent('AMAZON.CancelIntent')
def cancel():
    bye_text = render_template('bye')
    return statement(bye_text)


@ask.session_ended
def session_ended():
    return '{}', 200


if __name__ == '__main__':
    app.run()
