import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session, request

from dining import get_hall_id
from dining import get_dining_today
from dining import get_dining_tomorrow

# get_dining_today('2', 'Breakfast', 'Entrees')
print(get_dining_tomorrow('1', "Dinner", 'Entrees'))