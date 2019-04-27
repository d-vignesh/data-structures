
# program to store cities by their continents and countries using a list and dict

locations = {}

def add_city( city , continent , country ) :
	locations.setdefault( country , {})
	locations[country].setdefault( continent , [] )
	locations.get(country).get(continent).append(city)



cont = 'y'

while ( cont == 'y' ) :

	city = input(' enter city to add : ')
	continent = input(' enter the continent ')
	country = input(' enter the country ')

	add_city( city , continent , country )

	cont = input(' do you want to continue? ( y / n ) : ')

for country in locations.keys() :
	print(' country : ' + country)
	for continent , cities in locations[country].items() :
		print('\t continent : ' + continent )
		for city in cities :
			print('\t\t city : '+ city ) 

