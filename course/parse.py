import json
import xmltodict
from urllib.request import urlopen

def parse(link):
    f = urlopen(link)
    xmlString = f.read()
    jsonString = json.dumps(xmltodict.parse(xmlString), indent=4)
    return jsonString
