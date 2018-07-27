import urllib, json
from bs4 import BeautifulSoup
from urllib.request import urlopen
#from pandas import json

request = urlopen('http://wmon.cites.illinois.edu/listbuilding.html')
soup = BeautifulSoup(request, 'html.parser')
table = soup.find_all('table')[1] # Grab the 2 table
retval = []
for x in table.find_all('tr'):
	ret = {}	
	ret['buildingnumber'] = x.contents[1].string
	ret['buildingname'] = x.contents[3].string
	if (x.contents[5] is None):
	        ret['totalAP'] = None
	else:
		ret['totalAP'] = x.contents[5].string
	if (x.contents[11] is None):
        	ret['clientdevices'] = None
	else:
		ret['clientdevices'] = x.contents[11].string
	retval.append(ret)
finalreturn = {}
#final = retval[0]
#print(final)
finalreturn['data'] = retval[1:]
with open('wirelesschecker.json', 'w') as outfile:
	json.dump(finalreturn, outfile, sort_keys = True, indent = 4)
