#   6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 99) so
#   each person can have more than one favorite number. Then print each person’s
#   name along with their favorite numbers.


#   6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
#   Think of five names, and use them as keys in your dictionary. Think of a
#   favorite number for each person, and store each as a value in your
#   dictionary. Print each person’s name and their favorite number. For even
#   more fun, poll a few friends and get some actual data for your program.

favorite_numbers = {
    'Bella': 5,
    'Camryn': 7,
    'Ellis': 3,
    'Bob': 37,
    'David': 20
    }

print(f"Bella's favorite number is {favorite_numbers['Bella']}.")

number = favorite_numbers['Camryn']
print(f"\nCamryn's favorite number is {number}.")

number = favorite_numbers['Ellis']
print(f"\nEllis' favorite number is {number}.")

number = favorite_numbers['Bob']
print(f"\nBob's favorite number is {number}.")

number = favorite_numbers['David']
print(f"\nDavid's favorite number is {number}.")

favorite_numbers_multiples = {
    'Bella': [2, 4, 6, 8, 10],
    'Camryn': [1, 3, 5, 7, 9],
    'Ellis': [10, 20, 30, 40, 50],
    'Bob': [25, 50, 75, 100],
    'David': [100, 1000, 100000, 10000, 1],
    }

for person, numbers in favorite_numbers_multiples.items():
    print(f"\n{person.title()}'s favorite numbers are:")
    for number in numbers: 
        print(f"{number}")


