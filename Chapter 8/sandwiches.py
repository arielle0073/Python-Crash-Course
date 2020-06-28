#   8-12. Sandwiches: Write a function that accepts a list of items a person
#   wants on a sandwich. The function should have one parameter that collects as
#   many items as the function call provides, and it should print a summary of
#   the sandwich that’s being ordered. Call the function three times, using a
#   different number of arguments each time.

def build_a_sandwich(*toppings):
    """Print a summary of the sandwich being ordered."""
    print("\nHere's what I have for your order:")
    for topping in toppings:
        print(f"-{topping}")

build_a_sandwich('tomato', 'cheese', 'lettuce')
build_a_sandwich('zucchini')
build_a_sandwich('mayo', 'cheese', 'pickes')
