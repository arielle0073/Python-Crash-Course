#   7-3. Multiples of Ten: Ask the user for a number, and then report whether
#   the number is a multiple of 10 or not.

your_number = input("Please type a number: ")

your_number = int(your_number)

if your_number % 10 == 0: 
    print(f"Your number, {your_number}, is a multiple of 10.")
else: 
    print(f"Your number, {your_number}, is not a multiple of 10.")

