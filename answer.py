import logging
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session, request

from dining import get_dining


def answer_entrees(vegetarian):
    hall_id = session.attributes['hall_id']
    hall_name = session.attributes['hall_name']
    meal = session.attributes['meal']
    date = session.attributes['date']
    
    results = get_dining(date, hall_id, meal, 'Entrees', vegetarian)
    if not results == None and not results == []:
        answer_msg = render_template('answer-entrees-ask', 
            hall=hall_name, meal=meal, date=date,
            results=results
        )
    else:
        answer_msg = render_template('error-not-found')
    return question(answer_msg)


def answer_details(vegetarian):
    hall_id = session.attributes['hall_id']
    hall_name = session.attributes['hall_name']
    meal = session.attributes['meal']
    date = session.attributes['date']

    results_entrees     = get_dining(date, hall_id, meal, 'Entrees', vegetarian)
    results_starches    = get_dining(date, hall_id, meal, 'Starches', vegetarian)
    results_vegetables  = get_dining(date, hall_id, meal, 'Vegetables', vegetarian)
    results_soups       = get_dining(date, hall_id, meal, 'Soups', vegetarian)
    results_salads      = get_dining(date, hall_id, meal, 'Salads & Salad Bar', vegetarian)
    results_desserts    = get_dining(date, hall_id, meal, 'Desserts', vegetarian)
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
