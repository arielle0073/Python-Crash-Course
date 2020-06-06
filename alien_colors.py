#   Imagine an alient was just shot down in a game. Create a variable called
#   alien_color and assign it a value of 'green', 'yellow', or 'red'.

alien_color = 'yellow'


#   Write an if statement to test whether the alien's color is green. If it is,
#   print a message that the player just earned 4 points. Write one version of
#   this program that passes the if test and another that fails. (The version
#   that fails will have no output)

#   This version will fail. 
if alien_color == 'green':
    print("You just earned 4 points!")


alien_color = 'green'

#   This version will pass.
if alien_color == 'green':
    print("You just earned 10 points!")
