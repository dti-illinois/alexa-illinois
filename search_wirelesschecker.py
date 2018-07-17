import json
#import data.wirelesschecker_scrape
import wirelesschecker_scrape


def search_wirelesschecker(buildingname):
	#file = open('data/wirelesschecker.json', 'r')
	file = open('wirelesschecker.json', 'r')
	wirelesscheckers = json.load(file)['data']


	results = []
	for wirelesschecker in wirelesscheckers:
		#if buildingnumber  != None and buildingnumber  != wirelesscheckers['buildingnumber'].lower():  continue
		if buildingname   != None and buildingname.lower() != wirelesschecker['buildingname'].lower():   continue
		results.append(wirelesschecker)
	return results
