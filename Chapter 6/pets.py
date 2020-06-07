#   6-8. Pets: Make several dictionaries, where each dictionary represents a
#   different pet. In each dictionary, include the kind of animal and the
#   owner’s name. Store these dictionaries in a list called pets. Next, loop
#   through your list and as you do, print everything you know about each pet.


pet_1 = {
    'animal': 'puppy',
    'owner': 'Ally',
    }

pet_2 = {
    'animal': 'lizard',
    'owner': 'Alex',
    }

pet_3 = {
    'animal': 'bird',
    'owner': 'Cameron'
    }


pets = [pet_1, pet_2, pet_3]


#   Option 1 
for pet in pets: 
    animal = pet['animal']
    owner = pet['owner']
    print(f"This {animal} is cared for by {owner}.")

print("\n")

#   Option 2
for pet in pets:
    for key, value in pet.items(): 
        print(f"{key.title()}: {value.title()}")