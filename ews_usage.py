from urllib.request import urlopen
import json

EWS_URL = 'https://my.engr.illinois.edu/labtrack/util_data_json.asp'

def get_ews_usage():
    html = urlopen(EWS_URL).read().decode('utf-8')
    data = json.loads(html)['data']
    return data
