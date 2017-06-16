# create a mapping of state to abbreviation
states = {
    'Telangana' : 'TG',
    'Andhra Pradesh' : 'AP',
    'Maharashtra' : 'MH',
    'Uttar Pradesh' : 'UP',
    'Jammu & Kashmir' : 'JK'
}

# create a basic set of states and some cities in them
cities = {
    'TG' : 'Hyderabad',
    'AP' : 'Amaravati',
    'MH' : 'PUNE',
}

# add some more cities
cities['UP'] = 'Lukhnow'
cities['JK'] = 'Srinagar'

# print out some cities
print('-' * 10)
print("UP State has: ", cities['UP'])
print("JK State has: ", cities['JK'])

# print some states
print('-' * 10)
print("Jammu & Kashmir's abbreviation is: ", states['Jammu & Kashmir'])
print("Andhra Pradesh's abbreviation is: ", states['Andhra Pradesh'])

# do it by using the state then cities dict
print('-' * 10)
print("Jammu & Kashmir has: ", cities[states['Jammu & Kashmir']])
print("Andhra Pradesh has: ", cities[states['Andhra Pradesh']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

#print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# safely get an abbreviation by state that might not be there
state = states.get('Karnataka')

if not state:
    print("Sorry, no Karnataka.")

# get a city with a default value
city = cities.get('KA', 'Does Not Exist')
print(f"The city for the state 'KA' is: {city}")
