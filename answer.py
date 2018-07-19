import logging
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session, request

from courses import make_link
from courses import get_sections
from courses import get_crn
from courses import get_lecture_detail

# get all sections of corresponding course
# return a list of string
def answer_sections():
    year = session.attributes['year']
    semester = session.attributes['semester']
    subject = session.attributes['subject']
    course_num = session.attributes['course_num']
    link = make_link(year, semester, subject, course_num)
    temp_list = get_sections(link)
    return temp_list

# get all details of lectures
# return a statement / question
def answer_details():
    year = session.attributes['year']
    semester = session.attributes['semester']
    subject = session.attributes['subject']
    course_num = session.attributes['course_num']
    section = session.attributes['section']
    link = make_link(year, semester, subject, course_num)
    crn = get_crn(link, section)
    link = make_link(link, crn)
    result_dict = get_lecture_detail(link)

    course_title    =       result_dict['course_title']
    term            =       result_dict['term']
    start_date      =       result_dict['start_date']
    end_date        =       result_dict['end_date']
    start_time      =       result_dict['start_time']
    end_time        =       result_dict['end_time']
    days_of_week    =       result_dict['days_of_week']
    professor       =       result_dict['professor']

    answer_msg = render_template('answer-details',
                                 course_title=course_title, term=term, start_date=start_date,
                                 end_date=end_date, start_time=start_time, end_time=end_time,
                                 days_of_week=days_of_week,
                                 professor=professor, crn=crn)
    return question(answer_msg)
