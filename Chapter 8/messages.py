#   8-9. Messages: Make a list containing a series of short text messages. Pass
#   the list to a function called show_messages(), which prints each text
#   message.

def show_messages(texts): 
    """Show all text messages in a list."""
    for text in texts: 
        print(text)


texts = ['hello', 'hi', 'how are you', "what's up", 'good morning']
show_messages(texts)
