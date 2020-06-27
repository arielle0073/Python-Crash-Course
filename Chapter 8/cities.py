#   8-5. Cities: Write a function called describe_city() that accepts the name
#   of a city and its country. The function should print a simple sentence, such
#   as Reykjavik is in Iceland. Give the parameter for the country a default
#   value. Call your function for three different cities, at least one of which
#   is not in the default country.

def describe_city(city_name, city_country = 'spain'):
    """Display a sentence about the city.""" 
    message = (f'{city_name.title()} is in {city_country.title()}.\n')
    print(message)

describe_city('barcelona')
describe_city('madrid')
describe_city('paris', 'france')
