#   6-11. Cities: Make a dictionary called cities. Use the names of three cities
#   as keys in your dictionary. Create a dictionary of information about each
#   city and include the country that the city is in, its approximate
#   population, and one fact about that city. The keys for each city’s
#   dictionary should be something like country, population, and fact. Print the
#   name of each city and all of the information you have stored about it.


cities = {
    'barcelona': {
        'country': 'spain',
        'population': 5_586_000,
        'fact': 'In Barcelona, the official languages are Catalan and Spanish',
        },
    'milan': {
        'country': 'italy',
        'population': 3_140_000,
        'fact': 'In Milan, the official language is Italian',
        },
    'cairo': {
        'country': 'egypt',
        'population': 20_901_000,
        'fact': 'In Cairo, the official language is Arabic',
        },
    }

for city, info in cities.items(): 
    print(f"Here is some information about {city.title()}:")
    for fact_title, fact in info.items(): 
        print(f"{fact_title.title()}: {fact}")
    print("\n")

for city, info in cities.items(): 
    city_country = info['country']
    city_population = info['population']
    city_fact = info['fact']
    print(f"Here is some information about {city.title()}, in a different"
            " format")
    print(f"{city.title()} is located in {city_country.title()}")
    print(f"It has a population of approximately {city_population}") 
    print(f"{city_fact}\n")



