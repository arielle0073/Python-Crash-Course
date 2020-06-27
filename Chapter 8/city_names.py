#   8-6. City Names: Write a function called city_country() that takes in the
#   name of a city and its country. The function should return a string
#   formatted like this: "Santiago, Chile" Call your function with at least
#   three city-country pairs, and print the values that are returned.

def city_country(city_name, country_name):
    """Return a city and its country."""
    formatted_city_country = f"{city_name.title()}, {country_name.title()}"
    return formatted_city_country

city_1 = city_country('rome', 'italy')
print(city_1)

city_2 = city_country('nairobi', 'kenya')
print(city_2)

city_3 = city_country('cairo', 'egypt')
print(city_3)
