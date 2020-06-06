#	5-10. Checking Usernames: Do the following to create a program that
#   simulates how websites ensure that everyone has a unique username.

#   Make a list of five or more usernames called current_users.

current_users = ['cerulean', 'magenta', 'lavender', 'dandelion', 'rose']

#   Make another list of five usernames called new_users. Make sure one or
#   two of the new usernames are also in the current_users list.

new_users = ['MAGENTA', 'burnt_orange', 'robin_egg', 'grey', 'DaNDELion']


#   Loop through the new_users list to see if each new username has already
#   been used. If it has, print a message that the person will need to enter
#   a new username. If a username has not been used, print a message saying
#   that the username is available.

#   Make sure your comparison is case insensitive. If 'John' has been used,
#   'JOHN' should not be accepted. (To do this, you’ll need to make a copy of
#   current_users containing the lowercase versions of all existing users.)

# #   Option 1: 
# current_users_lower = []
# for current_user in current_users: 
#     current_users_lower.append(current_user.lower())

#   Option 2: 

current_users_lower = [current_user.lower() for current_user in current_users]

for new_user in new_users: 
    if new_user.lower() in current_users_lower: 
        print(f"Sorry, {new_user} is taken. Please enter a new username.\n")
    else:
        print(f"{new_user} is available!\n")



