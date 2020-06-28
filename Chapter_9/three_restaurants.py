#   9-2. Three Restaurants: Start with your class from Exercise 9-1. Create
#   three different instances from the class, and call describe_restaurant() for
#   each instance.


class Restaurant:
    """Create an instance of a restaurant.""" 


    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant.""" 
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type 


    def describe_restaurant(self): 
        """Describes the restaurant name and cuisine type."""
        message = f"{(self.restaurant_name)} serves {self.cuisine_type}."
        print(message)


    def open_restaurant(self): 
        """Tells that the restaurant is open.""" 
        print(f"{self.restaurant_name} is open.")


restaurant = Restaurant("Arnold's", "ice cream")
restaurant.describe_restaurant()


restaurant_two = Restaurant("Donny's", "pizza")
restaurant_two.describe_restaurant()

restaurant_three = Restaurant("Isaiah's", "sandwiches")
restaurant_three.describe_restaurant()




