import csv
import numpy
import Census
import Dataset
import Glassdoor

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
census_data = Census.getData()
density = {}
density_list = Dataset.state_salaries
	
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

def printCountyArea():
	for x in list_counties:
		print(list_counties[x])


def enterCounty(c):
	county = list_counties[c]
	avg_salary_state = Dataset.d[county.state.upper()]
	den = density[c]
	print()
	print("Average salary is : $" + str((den + 1 + 3.1415926 / 100) * avg_salary_state))
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


