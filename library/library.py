import json
from flask import render_template
from flask_ask import statement, question, session, request

import data


def ask_catalog():
	catalog = data.get_catalog()
	answer_msg = render_template(
		"answer-catalog", 
		catalog = catalog
	)
	return question(answer_msg)


def ask_with_date(library, date_str):
	info = data.get_all()
	# get library_id
	try:
		library_id = request.intent.slots.library.resolutions.resolutionsPerAuthority[0]['values'][0]['value']['id']
		# convert date
		temp = date_str.split('-')
		y, m, d = temp[0], temp[1], temp[2]
		calendar = data.get_calendar(library_id, y, m, d)
		# render template and answer
		answer_msg = render_template(
			"answer-date-calendar",
			year = y, month = m, date = d,
			calendar = calendar
		)
	except:
		answer_msg = render_template("error-other")
	return question(answer_msg)


def ask_next_seven_days(library):
	info = data.get_all()

	answer_msg = render_template()
	return question(answer_msg)
