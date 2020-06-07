#   6-3. Glossary: A Python dictionary can be used to model an actual
#   dictionary. However, to avoid confusion, let’s call it a glossary.

#   Think of five programming words you’ve learned about in the previous
#   chapters. Use these words as the keys in your glossary, and store their
#   meanings as values.

#   Print each word and its meaning as neatly formatted output. You might print
#   the word followed by a colon and then its meaning, or print the word on one
#   line and then print its meaning indented on a second line. Use the newline
#   character (\n) to insert a blank line between each word-meaning pair in your
#   output.

my_glossary = {
    'string': 'a series of characters',
    'list': 'a collection of items in a particular order',
    'tuple': 'an immutable list',
    'logical_error': 'the syntax is valid Python code, but the code does not\
produce the desired result because a problem occurs in its logic',
    'list_comprehension': 'combines the for loop and the creation of new elemen\
ts into one line'
    }

#   Long way: 
print(f"String: {my_glossary['string']}")

print(f"\nList: {my_glossary['list']}")

print(f"\nTuple: {my_glossary['tuple']}")

print(f"\nLogical error: {my_glossary['logical_error']}")

print(f"\nList comprehension: {my_glossary['list_comprehension']}")


#   Short way: 
print("\n\nThis is the more succint way:\n")
word = 'string'
print(f"{word.title()}: {my_glossary[word]}")

word = 'list'
print(f"\n{word.title()}: {my_glossary[word]}")

word = 'tuple'
print(f"\n{word.title()}: {my_glossary[word]}")

word = 'logical_error'
print(f"\n{word.title()}: {my_glossary[word]}")

word = 'list_comprehension'
print(f"\n{word.title()}: {my_glossary[word]}")
