from numpy import array,ones,linalg
from pylab import plot,show

import requests
                              # income     # var
census_variables = ['NAME', 'B01001_001E']

params = {
    'get': ','.join(census_variables),
    'for': 'state:*',
    'key': '06e757dc6f87325c515f0cd3f151fe20d3e647f1'
}
data = requests.get("http://api.census.gov/data/2015/acs1", params=params)
names = []
var = []
income = []


for row in data.json()[1:]:
    names.append(row[0])
    income.append(float(row[1]) // 100)

# print(var)
zipped = list(zip(names, income))

census_data = {}
for i in range(len(names)):
	census_data[names[i]] = income[i]

# print(census_data)

#print(state_income_by_housing)

def getData():
	return census_data

# print(state_income_by_housing)


# A = array([names, ones(len(names))])
# w = linalg.lstsq(A.T,y)[0]
# line = w[0]*names+w[1]
# plot(names, line,'r-',names,y,'o')
# show()

# sorted_income = sorted(income_by_state.items(), key=lambda x: x[1])
# print(sorted_income)