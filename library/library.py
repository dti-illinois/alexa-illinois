import json
import time
import data
from flask import render_template
from flask_ask import statement, question, session, request
from datetime import date


def ask_catalog():
    catalog = data.get_catalog()
    answer_msg = render_template(
        "answer-catalog", 
        catalog = catalog
    )
    return question(answer_msg)


def ask_basic_info(library):
    try:
        info = data.get_all()
        library_id = request.intent.slots.library.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['id']
        for library_info in info:
            if library_info['unit_id'] == int(library_id):
                email = library_info['contact_email']
                answer_msg = render_template(
                    "answer-basic-info", 
                    library = library,
                    info = library_info
                )
                break
    # No library matching / date matching
    except (KeyError, AttributeError) as e:
        answer_msg = render_template("error-no-match")
    # other errors
    except: answer_msg = render_template("error-other")
    return question(answer_msg)


def ask_with_date(library, date_str):
    try:
        library_id = request.intent.slots.library.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['id']
        date_arr = date_str.split('-')
        y, m, d = date_arr[0], date_arr[1], date_arr[2]
        calendar = data.get_calendar(library_id, y, m, d)
        answer_msg = render_template(
            "answer-with-date",
            year = y, month = m, date = d,
            library = library,
            calendar = calendar
        )
    # No library matching / date matching
    except (KeyError, AttributeError) as e:
        answer_msg = render_template("error-no-match")
    # other errors
    except: answer_msg = render_template("error-other")
    return question(answer_msg)


def ask_next_seven_days(library):
    try:
        library_id = request.intent.slots.library.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['id']
        today = date.today()
        y, m, d = str(today.year), str(today.month), str(today.day)
        calendar = data.get_calendar(library_id, y, m, d)
        answer_msg = render_template(
            "answer-next-seven-days",
            library = library,
            calendar = calendar
        )
    # No library matching / date matching
    except (KeyError, AttributeError) as e:
        answer_msg = render_template("error-no-match")
    # other errors
    except: answer_msg = render_template("error-other")
    return question(answer_msg)
