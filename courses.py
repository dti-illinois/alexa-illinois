import json
import urllib
from urllib.request import urlopen
from parse import parse

course_url = "https://courses.illinois.edu/cisapp/explorer/schedule"

#########################  BASIC FEATURE  ##################################
def make_link(year, semester, subject, courseIdx, section = None):
    link = course_url + "/" + year + "/" + semester + "/" + subject + "/" + courseIdx
    if section != None:
        link += "/" + section
    return link

def make_link(link, section):
    link += "/" + section
    return link

def get_sections(link):
    url = link + ".xml"
    jsonString = parse(url)
    json_items = json.loads(jsonString)
    list = [(lambda x: x["#text"])(x) for x in json_items["ns2:course"]["sections"]["section"]]
    return list

def get_lecture_detail(link):
    return




#########################  ADVANCED FEATURE  ##################################
def get_num_lecture(link):
    return 0

def get_lecture_sections():
    lec_sections = []
    return lec_sections

def get_num_discussion(link):
    return 0;

def get_discussion_sections(lect, link):
    dis_sections = []
    return dis_sections;
