from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

def lambda_handler(event, context):
    attributes = event['session']['attributes']



    return {
        "response": {
            "outputSpeech": {
                "text": "Fuck you", 
                "type": "PlainText"
            }, 
            "shouldEndSession": False
        }, 
        "sessionAttributes": {
            "numbers": [5, 6, 2]
        }, 
        "version": "1.0"
    }