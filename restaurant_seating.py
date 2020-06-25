#   7-2. Restaurant Seating: Write a program that asks the user how many people
#   are in their dinner group. If the answer is more than eight, print a message
#   saying they’ll have to wait for a table. Otherwise, report that their table
#   is ready.

dinner_group_number = input("How many people are in your dinner group?: ")

dinner_group_number = int(dinner_group_number)

if dinner_group_number > 8:
    print("Sorry, you'll have to wait for another table.")
else: 
    print("Great, your table is ready.")

