#   8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
#   by default with a message that reads I love Python. Make a large shirt and a
#   medium shirt with the default message, and a shirt of any size with a
#   different message.

def make_shirt(size = 'large', message = 'I love Python!'):
    """Displays a sentence summarizing the size of the shirt and the message
    printed on it"""
    print(f'\nThis should be a {size} t-shirt.')
    print(f'This shirt should say, "{message}"')


make_shirt()
make_shirt('medium')
make_shirt('small', 'WOW!')
