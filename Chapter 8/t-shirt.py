#   8-3. T-Shirt: Write a function called make_shirt() that accepts a size and
#   the text of a message that should be printed on the shirt. The function
#   should print a sentence summarizing the size of the shirt and the message
#   printed on it. Call the function once using positional arguments to make a
#   shirt. Call the function a second time using keyword arguments.

def make_shirt(size, message):
    """Displays a sentence summarizing the size of the shirt and the message
    printed on it"""
    print(f'\nThis should be a {size} t-shirt.')
    print(f'This shirt should say, "{message}"')


make_shirt('small', 'Love that for you!')
make_shirt(message = 'Love that for you!', size = 'small')
make_shirt(size = 'small', message = 'Love that for you!')

