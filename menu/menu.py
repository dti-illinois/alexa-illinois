import logging
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session, request

from data import get_dining


def answer_entrees(filters):
    hall = session.attributes['hall']
    hall_name = session.attributes['hall_name']
    meal = session.attributes['meal']
    date = session.attributes['date']
    
    results = get_dining(date, hall, meal, 'Entrees', filters)
    if not results == None and not results == []:
        answer_msg = render_template('answer-entrees-ask', 
            hall=hall_name, meal=meal, date=date,
            results=results
        )
    else:
        answer_msg = render_template('error-not-found')
    return question(answer_msg)


def answer_details(filters):
    hall = session.attributes['hall']
    hall_name = session.attributes['hall_name']
    meal = session.attributes['meal']
    date = session.attributes['date']

    results_entrees     = get_dining(date, hall, meal, 'Entrees', filters)
    results_starches    = get_dining(date, hall, meal, 'Starches', filters)
    results_vegetables  = get_dining(date, hall, meal, 'Vegetables', filters)
    results_soups       = get_dining(date, hall, meal, 'Soups', filters)
    results_salads      = get_dining(date, hall, meal, 'Salads & Salad Bar', filters)
    results_desserts    = get_dining(date, hall, meal, 'Desserts', filters)
    if not results_entrees == None and not results_entrees == []:
        answer_msg = render_template('answer-details', 
            hall=hall_name, meal=meal, date=date,
            results_entrees=results_entrees,
            results_starches=results_starches,
            results_soups=results_soups,
            results_vegetables=results_vegetables,
            results_salads=results_salads,
            results_desserts=results_desserts
        )
    else:
        answer_msg = render_template('error-not-found')
    return question(answer_msg)


def detail():
    try:
        return answer_details(session.attributes['filter'])
    except KeyError:
        return statement(render_template('error-other'))


def add_filter(filter_name):
    try:
        filter_name = request.intent.slots.filter_name.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['id']
        if filter_name not in session.attributes['filter'].keys():
            session.attributes['filter'][filter_name] = True
        else:
            session.attributes['filter'][filter_name] = not session.attributes['filter'][filter_name]
        filter_msg = render_template('filter', 
            filter_name=filter_name,
            flag=session.attributes['filter'][filter_name]
        )
        return question(filter_msg)
    except KeyError:
        return question(render_template('error-not-understand'))


def ask_main(hall_name, meal, date):
    try:
        # get all info from request
        hall = request.intent.slots.hall.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['id']
        meal = request.intent.slots.meal.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['id']
        date = request.intent.slots.date.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['id']
        # store them in the session
        session.attributes['hall'] = hall
        session.attributes['hall_name'] = hall_name
        session.attributes['meal'] = meal
        session.attributes['date'] = date
        return answer_entrees(session.attributes['filter'])
    except KeyError:
        return question(render_template('error-not-understand'))


def interactive():
    # init all variables
    if 'hall' in session.attributes.keys():
        session.attributes.pop('hall')
    if 'hall_name' in session.attributes.keys():
        session.attributes.pop('hall_name')
    if 'meal' in session.attributes.keys():
        session.attributes.pop('meal')
    if 'date' in session.attributes.keys():
        session.attributes.pop('date')
    # render template
    ask_hall_msg = render_template('inter-ask-hall')
    return question(ask_hall_msg)


def answer_hall(hall_name):
    try:
        # get hall id from request
        hall = request.intent.slots.hall.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['id']
        # store hall id and name into session
        session.attributes['hall'] = hall
        session.attributes['hall_name'] = hall_name
        # ask other not answered specs
        if 'hall_name' not in session.attributes.keys():
            ask_msg = render_template('inter-ask-hall')
        elif 'meal' not in session.attributes.keys():
            ask_msg = render_template('inter-ask-meal')
        elif 'date' not in session.attributes.keys():
            ask_msg = render_template('inter-ask-date')
        else:
            return answer_entrees(session.attributes['filter'])
        return question(ask_msg)
    except KeyError:
        return question(render_template('error-not-understand'))


def answer_meal(meal):
    try:
        # get meal name from request
        meal = request.intent.slots.meal.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['id']
        # store meal into session
        session.attributes['meal'] = meal
        # ask other not answered specs
        if 'hall_name' not in session.attributes.keys():
            ask_msg = render_template('inter-ask-hall')
        elif 'meal' not in session.attributes.keys():
            ask_msg = render_template('inter-ask-meal')
        elif 'date' not in session.attributes.keys():
            ask_msg = render_template('inter-ask-date')
        else:
            return answer_entrees(session.attributes['filter'])
        return question(ask_msg)
    except KeyError:
        return question(render_template('error-not-understand'))


def answer_date(date):
    try:
        # get date (today or tomorrow) from request
        date = request.intent.slots.date.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['id']
        # store date into session
        session.attributes['date'] = date
        # ask other not answered specs
        if 'hall_name' not in session.attributes.keys():
            ask_msg = render_template('inter-ask-hall')
        elif 'meal' not in session.attributes.keys():
            ask_msg = render_template('inter-ask-meal')
        elif 'date' not in session.attributes.keys():
            ask_msg = render_template('inter-ask-date')
        else:
            return answer_entrees(session.attributes['filter'])
        return question(ask_msg)
    except KeyError:
        return question(render_template('error-not-understand'))
