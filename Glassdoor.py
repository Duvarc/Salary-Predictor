import requests
import json

class Company:

	def __init__(self, name, rating):
		self.name = name
		self.rating = rating

	def __str__(self):
		return self.name + ": " + str(self.rating)

	def __repr__(self):
		return self.name + ": " + str(self.rating)


CONST_HEADER = "http://api.glassdoor.com/api/api.htm"
list_employers = []
params = {}
page_limit = 5

# Thanks to https://gist.github.com/rogerallen/1583593

abbrev = {
    'alabama': 'AL',
    'alaska': 'AK',
    'arizona': 'AZ',
    'arkansas': 'AR',
    'california': 'CA',
    'colorado': 'CO',
    'connecticut': 'CT',
    'delaware': 'DE',
    'florida': 'FL',
    'georgia': 'GA',
    'hawaii': 'HI',
    'idaho': 'ID',
    'illinois': 'IL',
    'indiana': 'IN',
    'iowa': 'IA',
    'kansas': 'KS',
    'kentucky': 'KY',
    'louisiana': 'LA',
    'maine': 'ME',
    'maryland': 'MD',
    'massachusetts': 'MA',
    'michigan': 'MI',
    'minnesota': 'MN',
    'mississippi': 'MS',
    'missouri': 'MO',
    'montana': 'MT',
    'nebraska': 'NE',
    'nevada': 'NV',
    'new Hampshire': 'NH',
    'new Jersey': 'NJ',
    'new Mexico': 'NM',
    'new York': 'NY',
    'north Carolina': 'NC',
    'north Dakota': 'ND',
    'ohio': 'OH',
    'oklahoma': 'OK',
    'oregon': 'OR',
    'pennsylvania': 'PA',
    'rhode Island': 'RI',
    'south Carolina': 'SC',
    'south Dakota': 'SD',
    'tennessee': 'TN',
    'texas': 'TX',
    'utah': 'UT',
    'vermont': 'VT',
    'virginia': 'VA',
    'washington': 'WA',
    'west Virginia': 'WV',
    'wisconsin': 'WI',
    'wyoming': 'WY',
}

params = {
    'v': "1",
    'format': 'json',
    't.p': '94453',
    't.k': 'eJHCDB4oK3a',
    'pn': 1,
    'ps': "100",
    'action': 'employers',
    'city': 'SanFrancisco,CA',
    'state':'',
    'q': 'Software',
    'userip': '136.152.142.39',
    'useragent': 'Mozilla/5.0'}

def setCity(c):
	params["city"] = c

def setState(s):
	params["state"] = s

def setPageLimit(p):
	page_limit = p

def getData():
	return requests.get(CONST_HEADER, params=params, headers={
	                               "User-Agent": 'Mozilla/5.0'}).json()
def printEmployers():
	for com in list_employers:
		print(com)

# initParams("1", "json")
def getEmployers():
	# Calculate first page
	data = getData()
	num_pages = data["response"]["totalNumberOfPages"]
	s = data["response"]["employers"]
	for x in s:
		list_employers.append(Company(x["name"], x["overallRating"]))


	# Calculate more pages if needed
	for i in range(2, min(page_limit, num_pages)):
		params['pn'] = i
		data = getData()
		s = data["response"]["employers"]
		for x in s:
			list_employers.append(Company(x["name"], x["overallRating"]))

def printEmployers():
	for c in list_employers[:10]:
		print(c)

def init(loc):
	params['city'] = loc.name
	getEmployers()
	list_employers.sort(key=lambda x : -x.rating)
	printEmployers()



