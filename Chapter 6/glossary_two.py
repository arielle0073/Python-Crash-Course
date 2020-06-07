#   6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
#   up the code from Exercise 6-3 (page 99) by replacing your series of print()
#   calls with a loop that runs through the dictionary’s keys and values. When
#   you’re sure that your loop works, add five more Python terms to your
#   glossary. When you run your program again, these new words and meanings
#   should automatically be included in the output.



my_glossary = {
    'string': 'a series of characters',
    'list': 'a collection of items in a particular order',
    'tuple': 'an immutable list',
    'logical_error': 'the syntax is valid Python code, but the code does not\
produce the desired result because a problem occurs in its logic',
    'list_comprehension': 'combines the for loop and the creation of new elemen\
ts into one line'
    }


for word, definition in my_glossary.items(): 
    print(f"{word.title()}: {definition}\n")

#   Add five more terms. 

my_glossary['dictionary'] = 'allows you to connect related pieces of information\
'
my_glossary['else_block'] = 'a catchall statement'
my_glossary['key'] = 'connected to a value'
my_glossary['key_value'] = 'can be a number, a string, a list, another dictionary'
my_glossary['key_value_pair'] = 'a set of values associated with each other'

#   Print the new glossary,

for word, definition in my_glossary.items(): 
    print(f"{word.title()}: {definition}\n")
