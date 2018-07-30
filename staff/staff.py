import logging
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session, request

from search_staff import search_staff


def answer_firstname(firstname):
    session.attributes['firstname'] = request.intent.slots.firstname.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['id']
    confirm_msg = render_template("confirm-clue", 
        which_name="first name", 
        name=firstname
    )
    return question(confirm_msg)


def answer_lastname(lastname):
    session.attributes['lastname'] = request.intent.slots.lastname.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['id']
    confirm_msg = render_template("confirm-clue", 
        which_name="last name", 
        name=lastname
    )
    return question(confirm_msg)


def answer_middlename(middlename):
    session.attributes['middlename'] = mrequest.intent.slots.middlename.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['id']
    confirm_msg = render_template("confirm-clue", 
        which_name="middle name", 
        name=middlename
    )
    return question(confirm_msg)


def start_search():
    if 'firstname' in session.attributes.keys():
        firstname = session.attributes['firstname']
    else:
        firstname = None
    if 'lastname' in session.attributes.keys():
        lastname = session.attributes['lastname']
    else:
        lastname = None
    if 'middlename' in session.attributes.keys():
        middlename = session.attributes['middlename']
    else:
        middlename = None
    results = search_staff(firstname, lastname, middlename)
    if len(results) == 0:
        answer_msg = render_template("answer-noresults")
    elif len(results) < 10:
        answer_msg = render_template("answer-results", 
            num_results=len(results),
            results=results
        )
    else:
        answer_msg = render_template("answer-manyresults", 
            num_results=len(results)
        )
    # clear all variables
    if 'firstname' in session.attributes.keys():
        session.attributes.pop('firstname')
    if 'lastname' in session.attributes.keys():
        session.attributes.pop('lastname')
    if 'middlename' in session.attributes.keys():
        session.attributes.pop('middlename')
    return question(answer_msg)