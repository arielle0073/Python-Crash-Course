# Write a series of conditional tests. Print a statement describing each test
# and your prediction for the results of each test. 

name = 'Ari'

#testing something
print(f"{name == 'Ari'}")

print("\nIs name.lower() == 'ari'? I predict True.")
print(name.lower() == 'ari')

print("\nIs name == 'ari'? I predict False.")
print(name == 'ari')

print("\nIs name == 'Paul'? I predict False.")
print(name == 'Paul')

print("\nIs name != 'Simi'? I predict True.")
print(name != 'Simi')

print("\nIs name == 'Ari' or 'Paul'? I predict True.")
print(name == 'Ari' or name == 'Paul')

age = 26

print('\nIs age >= 30? I predict False.')
print(age >= 30)

favorite_foods = ['plantains', 'ice cream', 'French fries', 'brussel sprouts']

print(f"\n{'french fries' in favorite_foods}")

print(f"\n{'French fries' in favorite_foods}")

print('cauliflower' not in favorite_foods)

