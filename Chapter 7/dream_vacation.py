#	7-10. Dream Vacation: Write a program that polls users about their dream
#	vacation. Write a prompt similar to If you could visit one place in the
#	world, where would you go? Include a block of code that prints the results
#	of the poll.

# SOLUTION 1 

# message = ""
# poll_results = {} 

# name_prompt = "What is your name? " 
# vacation_prompt = "If you could visit one place in the world, where would you go? "

# while message != 'no': 
#     name = input(name_prompt)
#     vacation_spot = input(vacation_prompt)
#     poll_results[name] = vacation_spot
#     message = input("Would you like to let another person respond? (yes/no) ")

# for name, vacation_spot in poll_results.items():
#     print(f"{name.title()} would like to visit {vacation_spot.title()}")

# SOLUTION 2

# poll_active = True 
# poll_results = {}

# name_prompt = "What is your name? " 
# vacation_prompt = "If you could visit one place in the world, where would you go? "

# while poll_active: 
#     name = input(name_prompt)
#     vacation_spot = input(vacation_prompt)
#     poll_results[name] = vacation_spot
#     message = input("Would you like to let another person respond? (yes/no) ")
#     if message == 'no':
#         poll_active = False 

# for name, vacation_spot in poll_results.items():
#     print(f"{name.title()} would like to visit {vacation_spot.title()}")


#   SOLUTION 3

name_prompt = "What is your name? " 
vacation_prompt = "If you could visit one place in the world, where would you go? "

poll_results = {}

while True: 
    name = input(name_prompt)
    vacation_spot = input(vacation_prompt)
    poll_results[name] = vacation_spot
    message = input("Would you like to let another person respond? (yes/no) ")
    if message == 'no':
        break

for name, vacation_spot in poll_results.items():
    print(f"{name.title()} would like to visit {vacation_spot.title()}")