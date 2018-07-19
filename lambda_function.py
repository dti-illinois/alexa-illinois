import logging
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session, request


from answer import answer_details
from answer import answer_sections


app = Flask(__name__)
ask = Ask(app, '/')
logging.getLogger("flask_ask").setLevel(logging.DEBUG)


def lambda_handler(event, _context):
    return ask.run_aws_lambda(event)


@ask.launch
def welcome():
    # init
    welcome_msg = render_template('welcome') #TODO: welcome template
    return question(welcome_msg)


@ask.intent("AMAZON.HelpIntent")
def help():
    help_msg = render_template('help')  #TODO: help template
    return question(help_msg)


@ask.intent("AMAZON.FallbackIntent")
def fallback():
    fallback_msg = render_template('error-not-understand') #TODO: fallback template
    return question(fallback_msg)


@ask.intent('AMAZON.CancelIntent')
@ask.intent("AMAZON.StopIntent")
def stop():
    goodbye_msg = render_template('goodbye') #TODO: goodbye template
    return statement(goodbye_msg)

# User says year (2018), and then will be redirected to AnswerSemesterIntent
@ask.intent('AnswerYearIntent', mapping={'year': 'year'})
def answer_year(year):
    try:
        # get year from request
        year = request.intent.slots.year.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['id']
        # store year into session
        session.attributes['year'] = year
        # ask other not answered specs
        if 'semester' not in session.attributes.keys():
            ask_msg = render_template('ask-semester')
        elif 'subject' not in session.attributes.keys():
            ask_msg = render_template('ask-subject')
        elif 'course_num' not in session.attributes.keys():
            ask_msg = render_template('ask-course_num')
        elif 'section' not in session.attributes.keys():
            ask_msg = render_template('ask-section')
        else:
            return answer_details()
        return question(ask_msg)
    except KeyError:
        err_msg = render_template()
        return statement(err_msg)
    #TODO: Define MissingValueError


# User says semester (fall), and then will be redirected to AnswerCourseNameIntent or AnswerSubjectIntent
@ask.intent('AnswerSemesterIntent', mapping={'semester': 'semester'})
def answer_semester():
    try:
        # get semester from request
        semester = request.intent.slots.semester.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['id']
        # store year into session
        session.attributes['semester'] = semester
        # ask other not answered specs
        if 'year' not in session.attributes.keys():
            ask_msg = render_template('ask-year')
        elif 'subject' not in session.attributes.keys():
            ask_msg = render_template('ask-subject')
        elif 'course_num' not in session.attributes.keys():
            ask_msg = render_template('ask-course_num')
        elif 'section' not in session.attributes.keys():
            ask_msg = render_template('ask-section')
        else:
            return answer_details()
        return question(ask_msg)
    except KeyError:
        ask_msg = render_template('error-not-understand')
        return question(ask_msg)


# User says course name (CS 225), and then will be redirected to AnswerSectionIntent
@ask.intent("AnswerCourseNameIntent")
def answer_course_name():
    try:
        # get subject and course_num from request
        subject = request.intent.slots.subject.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['id']
        course_num = request.intent.slots.course_num.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['id']
        # store year into session
        session.attributes['subject'] = subject
        session.attributes['course_num'] = course_num
        # ask other not answered specs
        if 'year' not in session.attributes.keys():
            ask_msg = render_template('ask-year')
        elif 'semester' not in session.attributes.keys():
            ask_msg = render_template('ask-semester')
        elif 'section' not in session.attributes.keys():
            ask_msg = render_template('ask-section')
        else:
            return answer_details()
        return question(ask_msg)
    except KeyError:
        err_msg = render_template('error-other')
        return statement(err_msg)

# User says subject name (C.S. or Computer Science), and then will be redirected to AnswerCourseNumIntent
@ask.intent("AnswerSubjectIntent")
def answer_subject():
    try:
        # get subject and course_num from request
        subject = request.intent.slots.subject.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['id']
        course_num = request.intent.slots.course_num.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['id']
        # store year into session
        session.attributes['subject'] = subject
        session.attributes['course_num'] = course_num
        # ask other not answered specs
        if 'year' not in session.attributes.keys():
            ask_msg = render_template('ask-year')
        elif 'semester' not in session.attributes.keys():
            ask_msg = render_template('ask-semester')
        elif 'section' not in session.attributes.keys():
            ask_msg = render_template('ask-section')
        else:
            return answer_details()
        return question(ask_msg)
    except KeyError:
        err_msg = render_template('error-other')
        return statement(err_msg)

# User says course number (225), and then will be redirected to AnswerSectionIntent
# However, for here, we will provide the detail of section name
@ask.intent("AnswerCourseNumIntent")
def answer_course_num():
    try:
        return answer_details(session.attributes['filter'])
    except KeyError:
        err_msg = render_template('error-other')
        return statement(err_msg)

# What user says will be section number and I have to find corresponding crn
@ask.intent("AnswerSectionIntent")
def answer_crn():
    try:
        return answer_details()
    except KeyError:
        err_msg = render_template('error-other')
        return statement(err_msg)

# TODO: try only if all above done
@ask.intent("AnswerMainIntent")
def answer_crn():
    try:
        return answer_details(session.attributes['filter'])
    except KeyError:
        err_msg = render_template('error-other')
        return statement(err_msg)

if __name__ == '__main__':
    app.run(debug=True)