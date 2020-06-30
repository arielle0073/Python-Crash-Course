#   9-5. Login Attempts: Add an attribute called login_attempts to your User
#   class from Exercise 9-3 (page 162). Write a method called
#   increment_login_attempts() that increments the value of login_attempts by 1.
#   Write another method called reset_login_attempts() that resets the value of
#   login_attempts to 0. Make an instance of the User class and call
#   increment_login_attempts() several times. Print the value of login_attempts
#   to make sure it was incremented properly, and then call
#   reset_login_attempts(). Print login_attempts again to make sure it was reset
#   to 0.


class User: 
    """Represent a user profile.""" 

    def __init__(self, first_name, last_name, email_address, birthday):
        """Initialize the user.""" 
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.birthday = birthday
        self.login_attempts = 0

    def describe_user(self): 
        """Print a summary of the user's information.""" 
        print(f"\nFirst name: {self.first_name.title()}")
        print(f"Last name: {self.last_name.title()}")
        print(f"Email address: {self.email_address}")
        print(f"Birthday: {self.birthday}")


    def greet_user(self): 
        """Print a personalized greeting to the user.""" 
        full_name = f"{self.first_name} {self.last_name}"
        print(f"\nWelcome, {full_name.title()}!")

    def increment_login_attempts(self):
        """Increments the value  of login attempts by 1."""
        self.login_attempts += 1 

    def reset_login_attempts(self):
        """Resets the value of login attempts to 0.""" 
        self.login_attempts = 0


user_one = User('david', 'williams', 'david@example.com', 'February 5')
user_one.describe_user()
user_one.greet_user()

user_one.increment_login_attempts()
user_one.increment_login_attempts()
user_one.increment_login_attempts()

print(f"\nNumber of login attempts: {user_one.login_attempts}")

user_one.reset_login_attempts()

print(f"Number of of login attempts after reset: {user_one.login_attempts}")


