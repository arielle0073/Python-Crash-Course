#   9-1. Restaurant: Make a class called Restaurant. The __init__() method for
#   Restaurant should store two attributes: a restaurant_name and a
#   cuisine_type. Make a method called describe_restaurant() that prints these
#   two pieces of information, and a method called open_restaurant() that prints
#   a message indicating that the restaurant is open. Make an instance called
#   restaurant from your class. Print the two attributes individually, and then
#   call both methods.

class Restaurant:
    """Create an instance of a restaurant.""" 


    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant.""" 
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type 


    def describe_restaurant(self): 
        """Describes the restaurant name and cuisine type."""
        print(self.restaurant_name)
        print(self.cuisine_type)


    def open_restaurant(self): 
        """Tells that the restaurant is open.""" 
        print(f"{self.restaurant_name} is open.")


restaurant = Restaurant("Veggies", "vegetarian")

print(f"My restaurant's name is {restaurant.restaurant_name}.")
print(f"My restaurant serves {restaurant.cuisine_type} food.")

restaurant.describe_restaurant()
restaurant.open_restaurant()
