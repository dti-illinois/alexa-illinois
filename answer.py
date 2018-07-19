import logging
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session, request

from courses import make_link
from courses import get_sections
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
    return