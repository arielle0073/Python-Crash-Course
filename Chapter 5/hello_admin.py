#   Exercise 5-8. Hello Admin: Make a list of five or more usernames, including the name 
#   'admin'. Imagine you are writing code that will print a greeting to each 
#   user after they log in to a website. Loop through the list, and print a 
#   greeting to each user:

#   If the username is 'admin', print a special greeting, such as Hello admin,
#   would you like to see a status report? Otherwise, print a generic greeting,
#   such as Hello Jaden, thank you for logging in again.

print("Part 1")
usernames = ['admin', 'jerry', 'bob', 'phillip', 'dan', 'alexis']

for username in usernames: 
    if username == 'admin':
        print(f"Hello {username.title()}, would you like to see a status report?\n")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.\n")

#   Exercise 5-9. No Users: Add an if test to hello_admin.py to make sure the
#   list of users is not empty.

#   If the list is empty, print the message We need to find some users!
#   Remove all of the usernames from your list, and make sure the correct message is printed.


usernames_two = usernames[:]

print("Part Two")
if usernames_two:
    for username in usernames_two: 
        if username == 'admin':
            print(f"Hello {username.title()}, would you like to see a status report?\n")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.\n")
else:
    print("We need to find some users!")
    
#   Remove all usernames from the list....

del(usernames_two[:])

#   Check to see if the correct message is printed.

print("Part Three")
if usernames_two:
    for username in usernames_two: 
        if username == 'admin':
            print(f"Hello {username.title()}, would you like to see a status report?\n")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.\n")
else:
    print("We need to find some users!")
