#   9-4. Number Served: Start with your program from Exercise 9-1 (page 162).
#   Add an attribute called number_served with a default value of 0. Create an
#   instance called restaurant from this class. Print the number of customers
#   the restaurant has served, and then change this value and print it again.

#   Add a method called set_number_served() that lets you set the number of
#   customers that have been served. Call this method with a new number and
#   print the value again.

#   Add a method called increment_number_served() that lets you increment the
#   number of customers who’ve been served. Call this method with any number you
#   like that could represent how many customers were served in, say, a day of
#   business.


class Restaurant: 
    """Represent a restaurant.""" 

    def __init__(self, restaurant_name, cuisine_type): 
        """Initialize the restaurant.""" 
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self): 
        """Print the restaurant name and cuisine type.""" 
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cusine type: {self.cuisine_type}")


    def open_restaurant(self): 
        """Prints a message saying the restaurant is open.""" 
        print(f"{self.restaurant_name} is open for business.")

    def set_number_served(self, number_served): 
        """Set the number of customers that have been served.""" 
        self.number_served = number_served 

    def increment_number_served(self, add_number_served): 
        """Add the given number to the number of customers served.""" 
        self.number_served += add_number_served


restaurant = Restaurant("Terry's", "soul food")

print(f"{restaurant.restaurant_name} has served {restaurant.number_served} "
    "customers.")

restaurant.number_served = 1_000_000 

print(f"\n{restaurant.restaurant_name} has served {restaurant.number_served} "
    "customers.")

restaurant.set_number_served(5_000_000)
print(f"\n{restaurant.restaurant_name} has served {restaurant.number_served} "
    "customers.")

restaurant.increment_number_served(10_000)
print(f"\n{restaurant.restaurant_name} has served {restaurant.number_served} "
    "customers.")



