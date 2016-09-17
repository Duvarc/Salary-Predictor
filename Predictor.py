import csv
import numpy
import geopy

import Census
import Dataset
import Glassdoor

from geopy.distance import vincenty

class County:

	def __init__(self, name, state, area, pop):
		self.name = name
		self.state = state
		self.area = area
		self.pop = pop

	def __str__(self):
		return self.name + " | " + self.state + " | " + str(self.area) + " | " + str(self.pop)

	def __repr__(self):
		return self.name + " | " + self.state + " | " + str(self.area) + " | " + str(self.pop)

list_counties = {}
counties_modifier = {}
census_data = Census.getData()
density = {}
density_list = Dataset.state_salaries
center = (39.8282, -98.5795)
	
def initDensity():
	for i in range(len(density_list)):
		density_list[i][0] = numpy.log10(density_list[i][0])
	minimum = min(density_list, key=lambda x: x[0])[0]
	maximum = float(max(density_list, key=lambda x: x[0])[0])
	for i in range(len(density_list)):
		density_list[i][0] = (density_list[i][0] - minimum) / maximum + 0.5

	for l in density_list:
		loc = l[1]
		loc = loc[:loc.index(",")]
		loc = " ".join(loc.split()[:-1])
		density[loc] = l[0]
	density['District of Columbia'] = density['District of']
	density.pop('District of', None)


def distanceToCenter(lat, lon):
	x = (lat, lon)
	return vincenty(x, center).miles

def readCSV():
	with open('County area/data.csv', encoding='utf-8', errors='ignore') as file:
		reader = csv.reader(file)
		for row in reader:
			state_name = row[5].replace("United States - ", "").split()[0]
			county_name = row[6].split()[:-1]
			county_name = " ".join(county_name)
			c = County(county_name, state_name, row[11], row[13])
			list_counties[county_name] = c
		list_counties['District of Columbia'] = list_counties['District of']
		list_counties.pop('District of', None)
	with open('County area/data2.csv', encoding='utf-8', errors='ignore') as file:
		reader = csv.reader(file)
		for row in reader:
			name = row[0].split()[:-1]
			name = " ".join(name)
			dist = distanceToCenter(float(row[2]), float(row[3]))
			pop = float(row[1])

			counties_modifier[name] = numpy.log10(pop) * 1000 + numpy.log10(2 ** (dist/1300)) * 300

			# Hardcoded Texas because distance heuristic should really be "proximity to US borders," however,
			# there was not enough time to code it and we had to settle for distance from the center. This is
			# accurate for places like San Francisco and New York, with distances of ~1500 miles, but undervalues
			# places like Houston, which is only 800 miles away but is very close to the US-Mexico border and an
			# increasing tech hub
			
			if name != "District of":
				if list_counties[name].state == "Texas":
					counties_modifier[name] += 3500


def printCountyArea():
	for x in list_counties:
		print(list_counties[x])


def enterCounty(c):
	county = list_counties[c]
	avg_salary_state = Dataset.d[county.state.upper()]
	den = density[c]
	print()
	salary = ((den + 0.9) * avg_salary_state + counties_modifier[c])
	print("Average salary is : $" + str(salary))
	print()
	print("Top rated employers in this area:")
	Glassdoor.init(county)

def init():
	readCSV()
	initDensity()



init()
try:
	name = input("Enter a county name: ")
	enterCounty(name)
except KeyError:
	print("Sorry! Could not find " + name + " County.")


