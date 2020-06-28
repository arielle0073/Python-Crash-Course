#   8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
#   Write a function called send_messages() that prints each text message and
#   moves each message to a new list called sent_messages as it’s printed. After
#   calling the function, print both of your lists to make sure the messages
#   were moved correctly.

def show_messages(texts): 
    """Show all text messages in a list."""
    print("All messages:")
    for text in texts: 
        print(text)

def send_messages(texts, sent_messages): 
    """Print each text message and move each message to sent_messages.""" 
    print("\nSending messages:")
    while texts: 
        text = texts.pop() 
        print(text)
        sent_messages.append(text)


texts = ['hello', 'hi', 'how are you', "what's up", 'good morning']
show_messages(texts)

sent_messages = []
send_messages(texts, sent_messages)

print("\nModified lists:")
print(texts)
print(sent_messages)