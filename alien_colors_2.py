#   Exercise 5-4: Choose a color for an alien as you did in Exercise 5-3, and write an if-else
#   chain. 

#   If the alien's color is green, print a statement that the player just earned 
#   5 points for shooting the alien.

#   If the alien's color isn't green, print a statement that the player just
#   earned 10 points.

#   Write one version of this program that runs the if block and another that
#   runs the else block. 

#   This version will run the else block.

alien_color = 'red'
print(alien_color)

if alien_color == 'green':
    print("You just earned 5 points!")
else: 
    print("You just earned 10 points!")


#   This version will run the if block. 

alien_color = 'green'
print(f"\n{alien_color}")

if alien_color == 'green':
    print("You just earned 5 points!")
else: 
    print("You just earned 10 points!")


#   Exercise 5-5: Turn your if-else chain from Exercise 5-4 into an if-elif-else
#   chain. 

#   If the alien is green, print a message that the player earned 5 points.

#   If the alien is yellow, print a message that the player earned 10 points.

#   If the alien is red, print a message that the player earned 15 points.

#   Write three versions of this program, making sure each message is printed
#   for the appropriate color alien.

#   Version 1. 

print("\n\nExercise 5-5")

alien_color = 'green'
print(f"\nThis alien is {alien_color}")

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")


alien_color = 'yellow'
print(f"\nThis alien is {alien_color}")

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")

alien_color = 'red'
print(f"\nThis alien is {alien_color}")

if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")



