#   9-3. Users: Make a class called User. Create two attributes called
#   first_name and last_name, and then create several other attributes that are
#   typically stored in a user profile. Make a method called describe_user()
#   that prints a summary of the user’s information. Make another method called
#   greet_user() that prints a personalized greeting to the user. Create several
#   instances representing different users, and call both methods for each user.

class User: 
    """Create an instance of a user.""" 


    def __init__(self, first_name, last_name, city):
        """Initialize the user.""" 
        self.first_name = first_name
        self.last_name = last_name 
        self.city = city


    def describe_user(self): 
        """Describe the user.""" 
        message = (f"{self.first_name.title()} {self.last_name.title()}")
        message += (f" from {self.city.title()}.")
        print(message)


    def greet_user(self):
        """Print a personalized greeting to the user.""" 
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}.")


user_one = User('ali', 'addison', 'miami')
user_one.describe_user()
user_one.greet_user()


print("\n")
user_two = User('bob', 'bobby', 'austin')
user_two.describe_user()
user_two.greet_user()

print("\n")
user_two = User('cadyn', 'camryn', 'los angeles')
user_two.describe_user()
user_two.greet_user()


