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

