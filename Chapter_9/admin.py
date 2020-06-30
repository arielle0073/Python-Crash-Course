#   9-7. Admin: An administrator is a special kind of user. Write a class called
#   Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
#   or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list
#   of strings like "can add post", "can delete post", "can ban user", and so
#   on. Write a method called show_privileges() that lists the administrator’s
#   set of privileges. Create an instance of Admin, and call your method.


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

#   OPTION 1
class Admin(User):
    """Represent an administrator profile.""" 


    def __init__(self, first_name, last_name, email_address, birthday): 
        """Initialize the administrator.""" 
        super().__init__(first_name, last_name, email_address, birthday)
        self.privileges = []

    def show_privileges(self): 
        """Displays the admin privileges.""" 
        print(f"\nAdmin privileges:")
        for privilege in self.privileges: 
            print(f"\t{privilege}")

my_admin_profile = Admin('arielle','waller', 'arielle@example.com',
     'December 12')

my_admin_profile.privileges = [
    'can add post',
    'can delete post',
    'can ban user'
    ]

my_admin_profile.describe_user()
my_admin_profile.show_privileges()


#   OPTION 2
class Admin(User):
    """Represent an administrator profile.""" 


    def __init__(self, first_name, last_name, email_address, birthday,
        *privileges): 
        """Initialize the administrator.""" 
        super().__init__(first_name, last_name, email_address, birthday)
        self.privileges = privileges 

    def show_privileges(self): 
        """Displays the admin privileges.""" 
        print(f"\nAdmin privileges:")
        for privilege in self.privileges: 
            print(f"\t{privilege}")

my_admin_profile = Admin('arielle','waller', 'arielle@example.com',
     'December 12', 'can post', 'can delete post', 'can ban user')

my_admin_profile.describe_user()
my_admin_profile.show_privileges()



