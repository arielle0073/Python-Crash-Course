#   7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
#   pizza toppings until they enter a 'quit' value. As they enter each topping, 
#   print a message saying you’ll add that topping to their pizza.

prompt = "\nPlease enter a topping for your pizza."
prompt += "\nWhen you are finished adding toppings, enter 'finished': "

#   Solution 1 
while True: 
    topping = input(prompt)
    if topping == 'finished':
        break
    print(f"Great, I will add {topping} to your pizza.")


#   Solution 2 
# active = True

# while active: 
#     topping = input(prompt)
#     if topping == 'finished': 
#         active = False 
#     else: 
#         print(f"Great, I will add {topping} to your pizza.")