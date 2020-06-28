#   8-11. Archived Messages: Start with your work from Exercise 8-10. Call the
#   function send_messages() with a copy of the list of messages. After calling
#   the function, print both of your lists to show that the original list has
#   retained its messages.

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

print("Using a copy of the list:")
send_messages(texts[:], sent_messages)

print("\n")
print(texts)
print(sent_messages)
