#   6-5. Rivers: Make a dictionary containing three major rivers and the country
#   each river runs through. One key-value pair might be 'nile': 'egypt'.

rivers = {
    'nile': 'egypt',
    'amazon': 'south america',
    'yangtze': 'china',
    }

#   Use a loop to print a sentence about each river, such as The Nile runs
#   through Egypt.

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

#   Use a loop to print the name of each river included in the dictionary.

#   Option 1
print("\nThis is Option 1:")
for river in rivers:
    print(river.title())

#   Option 2
print("\nThis is Option 2:")
for river in rivers.keys():
    print(river.title())

#   Use a loop to print the name of each country included in the dictionary.

print("\nThese are the names of each country in the dictionary:")
for country in rivers.values():
    print(country.title())
