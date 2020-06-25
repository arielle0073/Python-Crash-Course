#   6-9. Favorite Places: Make a dictionary called favorite_places. Think of
#   three names to use as keys in the dictionary, and store one to three
#   favorite places for each person. To make this exercise a bit more
#   interesting, ask some friends to name a few of their favorite places.
#   Loop through the dictionary, and print each person’s name and their favorite
#   places.

favorite_places = {
    'david': ['Miami', 'Los Angeles', 'Chicago'],
    'alexis': ['Dubai', 'Greece', 'Galapagos Islands'],
    'moira': ['Paris', 'Milan', 'Barcelona']
    }

for person, places in favorite_places.items():
    print(f"\n{person.title()}'s favorite places are:")
    for place in places: 
        print(f"{place}")
