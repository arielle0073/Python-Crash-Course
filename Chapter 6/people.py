#   6-7. People: Start with the program you wrote for Exercise 6-1 (page 99).
#   Make two new dictionaries representing different people, and store all three
#   dictionaries in a list called people. Loop through your list of people. As
#   you loop through the list, print everything you know about each person. 


#   6-1. Person: Use a dictionary to store information about a person you know.
#   Store their first name, last name, age, and the city in which they live.
#   You should have keys such as first_name, last_name, age, and city. Print
#   each piece of information stored in your dictionary.

singer = {
    'first_name': 'Lea',
    'last_name': 'Salonga',
    'age': '49',
    'city': 'Manila',
    }

# print(singer['first_name'])
# print(singer['last_name'])
# print(singer['age'])
# print(singer['city'])

singer_two = {
    'first_name': 'Denee',
    'last_name': 'Benton',
    'age': '28',
    'city': 'Winter Park',
    }

singer_three = {
    'first_name': 'Lauryn',
    'last_name': 'Hill',
    'age': '45',
    'city': 'South Orange',
    }

people_list = [singer, singer_two, singer_three]

# for person in people_list: 
#     print(person)

for person in people_list: 
    first_name = person['first_name']
    last_name = person['last_name']
    age = person['age']
    city = person['city']
    print(f"{first_name} {last_name} is from {city} and is {age} years old.")    







