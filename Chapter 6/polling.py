favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print(favorite_languages)

language = favorite_languages['sarah'].title()

print(f"Sarah's favorite language is {language}.")


print(f"Phil's favorite language is {favorite_languages['phil'].title()}\n\n")


for person, language in favorite_languages.items():
    print(f"Person: {person.title()}")
    print(f"Favorite Language: {language.title()}\n")


for name in favorite_languages.keys():
    print(name.title())


for name in favorite_languages:
    print(name.title())


take_the_poll = ['caroline', 'adam', 'gerard', 'johnny', 'edward', 'sarah',
'moira', 'phil']

for name in take_the_poll: 
    if name in favorite_languages.keys(): 
        print(f"\n{name.title()}, thank you for taking the poll!")
    else: 
        print(f"\n{name.title()}, please take this poll.")