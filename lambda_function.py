import logging
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session, request


from answer import answer_class_details
from answer import answer_course_details

from courses import make_prelink
from courses import get_sections


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
            ask_msg = render_template('ask-course')
        elif 'course_num' not in session.attributes.keys():
            ask_msg = render_template('ask-course_num')
        elif 'section' not in session.attributes.keys():
            ask_msg = render_template('ask-section')
        else:
            return answer_class_details()
        return question(ask_msg)
    except KeyError:
        err_msg = render_template("error-not-understand")
        return question(err_msg)
    #TODO: Define MissingValueError


# User says semester (fall), and then will be redirected to AnswerCourseNameIntent or AnswerSubjectIntent
@ask.intent('AnswerSemesterIntent', mapping={'semester': 'semester'})
def answer_semester(semester):
    try:
        # get semester from request
        semester = request.intent.slots.semester.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['id']
        # store year into session
        session.attributes['semester'] = semester
        # ask other not answered specs
        if 'year' not in session.attributes.keys():
            ask_msg = render_template('ask-year')
        elif 'subject' not in session.attributes.keys():
            ask_msg = render_template('ask-course')
        elif 'course_num' not in session.attributes.keys():
            ask_msg = render_template('ask-course_num')
        elif 'section' not in session.attributes.keys():
            ask_msg = render_template('ask-section')
        else:
            return answer_class_details()
        return question(ask_msg)
    except KeyError:
        ask_msg = render_template('error-not-understand')
        return question(ask_msg)


# User says course name (CS 225), and then will be redirected to AnswerSectionIntent
@ask.intent("AnswerCourseNameIntent", mapping={"subject": "subject", "courseNum": "course_num"})
def answer_course_name(subject, course_num):
    try:
        # get subject and course_num from request
        subject = request.intent.slots.subject['value']
        course_num = request.intent.slots.courseNum['value']
        # store year into session
        session.attributes['subject'] = subject
        session.attributes['course_num'] = course_num
        # ask other not answered specs
        if 'year' not in session.attributes.keys():
            ask_msg = render_template('ask-year')
        elif 'semester' not in session.attributes.keys():
            ask_msg = render_template('ask-semester')
        elif 'section' not in session.attributes.keys():
            link = make_prelink(year=session.attributes['year'], semester=session.attributes['semester'], subject=subject, courseIdx=course_num)
            sections = get_sections(link)
            ask_msg = render_template('ask-section', subject = subject, course_num=course_num, sections=sections)
        else:
            return answer_class_details()
        return question(ask_msg)
    except KeyError:
        err_msg = render_template("error-not-understand")
        return question(err_msg)

@ask.intent("AnswerCourseDescriptionIntent")
def answer_course_des():
    try:
        return answer_course_details()
    except:
        return


# User says subject name (C.S. or Computer Science), and then will be redirected to AnswerCourseNumIntent
@ask.intent("AnswerSubjectIntent", mapping={"subject": "subject"})
def answer_subject():
    try:
        # get subject from request
        subject = request.intent.slots.subject.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['id']
        # store year into session
        session.attributes['subject'] = subject
        # ask other not answered specs
        if 'year' not in session.attributes.keys():
            ask_msg = render_template('ask-year')
        elif 'semester' not in session.attributes.keys():
            ask_msg = render_template('ask-semester')
        elif 'course_num' not in session.attributes.keys():
            ask_msg = render_template('ask-course_num')
        elif 'section' not in session.attributes.keys():
            ask_msg = render_template('ask-section')
        else:
            return answer_class_details()
        return question(ask_msg)
    except KeyError:
        err_msg = render_template("error-not-understand")
        return question(err_msg)

# User says course number (225), and then will be redirected to AnswerSectionIntent
# However, for here, we will provide the detail of section name
@ask.intent("AnswerCourseNumIntent", mapping={"course_num": "course_num"})
def answer_course_num():
    try:
        # get course_num from request
        course_num = request.intent.slots.course_num.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['id']
        # store year into session
        session.attributes['course_num'] = course_num
        # ask other not answered specs
        if 'year' not in session.attributes.keys():
            ask_msg = render_template('ask-year')
        elif 'semester' not in session.attributes.keys():
            ask_msg = render_template('ask-semester')
        elif 'subject' not in session.attributes.keys():
            ask_msg = render_template('ask-course')
        elif 'section' not in session.attributes.keys():
            ask_msg = render_template('ask-section')
        else:
            return answer_class_details()
        return question(ask_msg)
    except KeyError:
        err_msg = render_template("error-not-understand")
        return question(err_msg)

# What user says will be section number and I have to find corresponding crn
@ask.intent("AnswerSectionIntent", mapping={"section": "section"})
def answer_section():
    try:
        # get course_num from request
        section = request.intent.slots.section.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['name']
        # store year into session
        session.attributes['section'] = section
        return answer_class_details()
    except KeyError:
        err_msg = render_template("error-not-understand")
        return question(err_msg)


@ask.intent("RestartIntent")
def restart():
    try:
        # clean the session attributions
        session.attributes = {}
        answer_msg = render_template("restart")
        return question(answer_msg)
    except KeyError:
        err_msg = render_template("ask-restart")
        return question(err_msg)

if __name__ == '__main__':
    app.run(debug=True)