#dicts - hashes - dictionaries Ex. stuff = {"states": state, "key" : key }

states = {
	'Oregon': 'OR', 
	'Florida': 'FL', 
	'California': 'CA', 
	'New York': 'NY', 
	'Michigan': 'MI'
}

cities = {
	'CA': 'San Francisco', 
	'MI': 'Detroit', 
	'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland’

print '-' * 10 
print 'NY state has: ', cities['NY']
print 'OR state has: ', cities['OR']

print '-' * 10 
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

print '-' * 10 
print 'Michigan has: ", cities[states['Michigan']]
print 'Florida has: ", cities[states['Florida']]

print '-' * 10 
#Putting two variables in a for loop is possible?!!?
for state, abbrev in states.items():
	print "%s has the city %s" % (state, abbrev)

print '-' * 10 
#It is posible
for abbrev, city in cities.items()
	print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 10 
state = states.get('Texas')

if not state: 
	print "Sorry, no Texas." 

city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city