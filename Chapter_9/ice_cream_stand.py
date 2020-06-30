#   9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant.
#   Write a class called IceCreamStand that inherits from the Restaurant class
#   you wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either
#   version of the class will work; just pick the one you like better. Add an
#   attribute called flavors that stores a list of ice cream flavors. Write a
#   method that displays these flavors. Create an instance of IceCreamStand, and
#   call this method.


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

#   OPTION 1 
# class IceCreamStand(Restaurant):
#     """Represent an ice cream stand.""" 


#     def __init__(self, restaurant_name, cuisine_type, *flavors): 
#         """
#         Initialize attributes of the parent class. 
#         Initialize attributes specific to the ice cream stand.
#         """ 
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors = flavors 


#     def display_flavors(self): 
#         """Display all flavors.""" 
#         print(f"\nThis ice cream stand has the following flavors:")
#         for flavor in self.flavors: 
#             print(f"\t{flavor}")


# my_icecream_stand = IceCreamStand('Cinci Ice Cream', 'ice cream', 'coffee', 
#         'chocolate', 'tres leches', 'chocolate chip cookie dough')
# my_icecream_stand.display_flavors()

#   OPTION 2
class IceCreamStand(Restaurant):
    """Represent an ice cream stand.""" 


    def __init__(self, restaurant_name, cuisine_type='ice cream'): 
        """
        Initialize attributes of the parent class. 
        Initialize attributes specific to the ice cream stand.
        """ 
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []


    def display_flavors(self): 
        """Display all flavors.""" 
        print(f"\nThis ice cream stand has the following flavors:")
        for flavor in self.flavors: 
            print(f"\t{flavor}")


my_icecream_stand = IceCreamStand('Cinci Ice Cream')
my_icecream_stand.flavors = ['Cinci Ice Cream', 'ice cream', 'coffee', 
    'chocolate', 'tres leches', 'chocolate chip cookie dough']
my_icecream_stand.display_flavors()
my_icecream_stand.describe_restaurant()

