#   8-14. Cars: Write a function that stores information about a car in a
#   dictionary. The function should always receive a manufacturer and a model
#   name. It should then accept an arbitrary number of keyword arguments. Call
#   the function with the required information and two other name-value pairs,
#   such as a color or an optional feature. Your function should work for a call
#   like this one:
#   car = make_car('subaru', 'outback',
#   color='blue', tow_package=True) Print the dictionary that’s returned to make
#   sure all the information was stored correctly.

#   SOLUTION 1: 

def make_car(manufacturer, model, **extras):
    """Store information about a car in a dictionary."""
    extras['manufacturer'] = manufacturer
    extras['model'] = model
    return extras

car = make_car('subaru', 'outback', color= 'blue', tow_package= True)
print(car)

#   SOLUTION 2 

def make_car_2(manufacturer, model, **extras):
    """Store information about a car in a dictionary."""
    car_description = {
        'manufacturer': manufacturer,
        'model': model,
        }
    for key, value in extras.items():
        car_description[key] = value
    return car_description


car = make_car_2('subaru', 'outback', color= 'blue', tow_package= True)
print(car)
