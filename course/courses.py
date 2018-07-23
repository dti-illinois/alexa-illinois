import json
import urllib
from urllib.request import urlopen
from parse import parse
from sets import Set

course_url = "https://courses.illinois.edu/cisapp/explorer/schedule"

subject = Set([])

#########################  BASIC FEATURE  ##################################
def make_prelink(year, semester, subject, courseIdx, section = None):
    link = course_url + "/" + year + "/" + semester + "/" + subject + "/" + courseIdx
    if section != None:
        link += "/" + section
    return link

def make_link(link, crn):
    link += "/" + crn
    return link

def get_sections(link):
    url = link + ".xml"
    jsonString = parse(url)
    json_items = json.loads(jsonString)
    list = [(lambda x: x["#text"])(x) for x in json_items["ns2:course"]["sections"]["section"]]
    return list

def get_crn(link, section):
    url = link + ".xml"
    jsonString = parse(url)
    json_items = json.loads(jsonString)
    sections = json_items["ns2:course"]["sections"]["section"]
    crn = next(item for item in sections if item['#text'] == section)['@id']
    return crn

#TODO: add ", and" for last one
def get_days_of_week(days):
    if days == "n.a":
        return ["unknown"]
    list_of_days = []
    for c in days:
        if c == 'M':
            list_of_days.append("Monday")
        elif c == "T":
            list_of_days.append("Tuesday")
        elif c == "W":
            list_of_days.append("Wednesday")
        elif c == "R":
            list_of_days.append("Thursday")
        elif c == "F":
            list_of_days.append("Friday")
    return list_of_days

def get_professors(prof):
    list_of_prof = []
    for item in prof["instructor"]:
        name = "Professor " + item['@lastName']
        list_of_prof.append(name)
    return list_of_prof

def get_lecture_detail(link):
    dict = {}
    url = link + ".xml"
    jsonString = parse(url)
    json_items = json.loads(jsonString)

    course_title = json_items["ns2:section"]["parents"]["course"]["#text"]
    start_date = json_items["ns2:section"]["startDate"][0:10]
    end_date = json_items["ns2:section"]["endDate"][0:10]
    start_time = json_items["ns2:section"]["meetings"]["meeting"]["start"]
    end_time = json_items["ns2:section"]["meetings"]["meeting"]["end"]
    days_of_week = json_items["ns2:section"]["meetings"]["meeting"]["daysOfTheWeek"]
    professor = json_items["ns2:section"]["meetings"]["meeting"]["instructors"]
    location = json_items["ns2:section"]["meetings"]["meeting"]["buildingName"]

    days_of_week = get_days_of_week(days_of_week)
    professor = get_professors(professor)

    dict["course_title"] = course_title
    dict["start_date"] = start_date
    dict["end_date"] = end_date
    dict["start_time"] = start_time
    dict["end_time"] = end_time
    dict["days_of_week"] = days_of_week
    dict["professor"] = professor
    dict["location"] = location

    return dict

def get_course_detail(link):
    dict = {}
    url = link + ".xml"
    jsonString = parse(url)
    json_items = json.loads(jsonString)

    course_title = json_items["ns2:course"]["label"]
    description = json_items["ns2:course"]["description"]
    description = description[0: description.find("Prerequisite")]
    credit = json_items["ns2:course"]["creditHours"]
    courseSectionInformation = json_items["ns2:course"]["courseSectionInformation"]
    genEdCategories = json_items["ns2:course"]

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
