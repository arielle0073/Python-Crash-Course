#   Photo Filter 3-1: RGB Colors
#   In one of the most common formats, a color is represented as a set of three
#   values from 0-255. Each value represents how much red, green, and blue light 
#   to mix when displaying a pixel. The color [255, 0, 0] represents the
#   brightest possible red, [0, 255, 0] represents bright green, and [0, 0, 255]
#   represents blue. In this model [0, 0, 0] represents black, and [255, 255,
#   255] represents white. Taken altogether, this model makes 256**3 (almost 17
#   million) possible colors.

#   Use a color picker to find a color you like. Store the RGB values for this
#   color in a list. Print each of these component values.

cerulean_rgb = [66, 197, 245]

red_value = cerulean_rgb[0]
green_value = cerulean_rgb[1]
blue_value = cerulean_rgb[2]

print("Cerulean RGB values")
print(f"\tRed: {red_value}")
print(f"\tGreen: {green_value}")
print(f"\tBlue: {blue_value}")

#   Photo Filter 3-2: HSL Colors
#   The HSL format represents colors as three components as well. In this model
#   the values correspond to the hue, saturation, and lightness of each pixel.
#   Most online color choosers will give you the RGB or HSL values for any color
#   you’re interested in.

#   Using the color picker you worked with in Challenge 3-1, store the HSL
#   values for your color in a list. Print each of these component values.


cerulean_hsl = [196, 90, 61] 

hue = cerulean_hsl[0]
saturation = cerulean_hsl[1]
lightness = cerulean_hsl[2]

print("\nCerulean HSL Values")
print(f"\tHue: {hue}")
print(f"\tSaturation: {saturation}")
print(f"\tLightness: {lightness}")

#   Photo Filter 3-3: Hex Colors
#   Another format stores individual colors as a hexadecimal string. In this
#   model, each value ranges from 00 to FF. If you’re unfamiliar with
#   hexadecimal numbers, they start at 0 and keep going past nine; it’s a
#   base-16 number system, as opposed to the base-10 system most of us are
#   accustomed to. In this system 00 represents 0, and FF represents 255, so you
#   can represent just as many colors in hexadecimal as you can in the 0-255
#   format. The advantage is that each color is represented as a six-character
#   string, typically preceeded by a # sign. The brightest red is '#ff0000',
#   bright green is '#00ff00', and bright blue is '#0000ff'.

#   Pick three colors you like, and store them in a list using the hexadecimal
#   color representation. Print each color.

colors_hexadecimal = ['#f5429b', '#42f5b6', '#6042f5']

print("\nThree Hexadecimal Colors:")
for color in colors_hexadecimal:
    print(f"\t{color}")


#   Photo Filter 3-4: RGB Decimal Colors
#   In some programs, RGB colors are represented using values from 0 to 1. In
#   this model [1, 0, 0] represents bright red, [0, 1, 0] represents bright
#   green, and blue is [0, 0, 1]. A darker red would be [0.75, 0, 0].

#   Choose a color you like, and store its RGB values in a list, in decimal
#   format. Print each component value.

#   Greenish
color_rgb_decimal = [0.1, 0.9, 0.6]

red_rgb_decimal = color_rgb_decimal[0]
green_rgb_decimal = color_rgb_decimal[1]
blue_rgb_decimal = color_rgb_decimal[2]

print("\nRGB Decimal Color")
print(f"\tRed: {red_rgb_decimal}")
print(f"\tGreen: {green_rgb_decimal}")
print(f"\tBlue: {blue_rgb_decimal}")

#   Photo Filter 3-5: RGBa Colors
#   In this model there’s a fourth value for each color, which is called alpha.
#   This fourth value controls the opacity or transparency of the pixel. Higher 
#   alpha values are more opaque, and lower values are more transparent. The
#   alpha component is usually a decimal value between 0 and 1, regardless of
#   what system is used for defining the RGB components.

#   Choose a color you like, and store its RGBa component values in a list.
#   Print the value of each component.

#   Purple
color_rgba = [154, 39, 236, 0,87]
red_rgba = color_rgba[0]
green_rgba = color_rgba[1]
blue_rgba = color_rgba[2]
opacity_rgba = color_rgba[3]

print("\nRGBa Color")
print(f"\tRed: {red_rgba}")
print(f"\tGreen: {green_rgba}")
print(f"\tBlue: {blue_rgba}")
print(f"\tOpacity: {opacity_rgba}")


#   Photo Filter 4-1: Single Color Loop
#   Choose a color format that you want to work with. Choose a color that you
#   like, and store its component values in a list. Write a loop that prints out
#   each of the component values.

pink_rgb = [196, 12, 159]

print("\nHere are the RGB values for my color:")
for value in pink_rgb:
    print(f"\t{value}")


#   Photo Filter 4-2: Modified Color
#   Start with a color you like, and store its component values in a list. Make
#   a new color based on the original color. You can do this in a for loop, or 
#   in a comprehension.

#   Print the original color, and the modified color.

original_color_rgb = [12, 55, 196]

print("\nHere are the RBG values for an original color: ")
for value in original_color_rgb:
    print(f"\t{value}")

# Via a for loop.

new_color = []
for value in original_color_rgb:
    new_color_value = value - 11 
    new_color.append(new_color_value)

print("\nHere are the RGB values for a new color, based on the original color, "
        "using a for loop: ")
for value in new_color: 
    print(f"\t{value}")

#   Via a list comprehension. 

modified_color = [value + 8 for value in original_color_rgb]

print("\nHere are the RGB values for a modified color, based on the original "
        "color, using a list comprehnsion:")

for value in modified_color:
    print(f"\t{value}")



#   Photo Filter 4-3: Grays
#   In digital color models, shades of gray are colors where the RGB component
#   values are all equal. When converting a non-gray color to a shade of gray,
#   there are a variety of ways to do this conversion, and each will usually
#   result in a different shade of gray.

#   Start with a color you like, and store its component values in a list. Make
#   the following new colors, based on your original color:

starting_color = [12, 159, 196]

print("\nHere is my starting color:")
for value in starting_color:
    print(f"\t{value}")

#   avg_gray: Find the average of the three RGB values, and use this value for
#   all three RGB values of the new color.

modified_starting_color = [] 
for value in starting_color: 
    average_starting_color = sum(starting_color)/len(starting_color)
    modified_starting_color.append(average_starting_color)

print("\nHere is my modified starting color (1), based on the average:")
for value in modified_starting_color:
    print(f"\t{value}")

# With a list comprehension 
mdc_two = [sum(starting_color)/len(starting_color) for value in range(3)]


#   max_gray: Find the maximum of the three RGB values, and use this value for
#   all three RGB values of the new color.

modified_starting_color_2 = [max(starting_color) for value in range(3)]
print("\nHere is my modified starting color (2), based on the maximum:")
for value in modified_starting_color_2:
    print(f"\t{value}")

#   min_gray: Find the minimum of the three RGB values, and use this value for
#   all three RGB values of the new color.

modified_starting_color_3 = [min(starting_color) for value in range(3)]
print("\nHere is my modified starting color (3), based on the minimum:")
for value in modified_starting_color_3:
    print(f"\t{value}")

#   r_gray: Use the red component of the original color as the value for all
#   three RGB values of the new color.

modified_starting_color_3 = [starting_color[0] for value in range(3)]
print("\nHere is my modified starting color (4), based on the red component:")
for value in modified_starting_color_3:
    print(f"\t{value}")

#   Print your original color, and each shade of gray based on that color.

#   Photo Filter 4-4: Bumped Reds
#   Let’s say we wanted to brighten only the red values in an image. We could do
#   this by adding a certain amount to the red component, or multiplying the red
#   component by a value greater than one. Start with a color you like. Make a
#   new color by increasing the value of the red component by a set amount. Make
#   a second new color by multiplying the value of the red component by a value
#   such as 1.1. Print your original color, and your two new colors. 


initial_color = [12, 50, 100]

new_color = initial_color[:]
    
new_color[0] = new_color[0]*3

new_color_2 = initial_color[:]

new_color_2[0] = new_color_2[0]*1.1

print("\nHere is my initial color:")
for value in initial_color:
    print(f"\t{value}")


print("\nHere is my new color with a red value brightened by a factor of 3:")
for value in new_color:
    print(f"\t{value}")


print("\nHere is my new color with a red value brightened by a factor of 1.1")
for value in new_color_2:
    print(f"\t{value}")


#   Photo Filter 4-6: Brightening Colors
#   To make an individual pixel brighter, you need to increase the values of all
#   three components. You can do this in a variety of ways.

#   Start with a color you like. Make a new color by adding a set amount to each
#   of the component values in your original color. Make a second new color by
#   multiplying each of the component values by a certain amount. Print your
#   original color, and your two new colors.

dull_color = [2, 4, 6]
print("\nHere is my original color:")
for value in dull_color:
    print(f"\t{value}")

bright_color = [value + 10 for value in dull_color]
print("\nHere is my brighter color, via adding a set amount to each component:")
for value in bright_color:
    print(f"\t{value}")

print("\nHere is my brighter color (2), via multiplying each component value by"
        " a set amount:")
bright_color_2 = [value * 20 for value in dull_color]
for value in bright_color_2:
    print(f"\t{value}")


#   Photo Filter 4-7: Hex Components
#   The advantage of representing colors in the hexadecimal format is that each
#   color can be represented by a single six-character string, or seven with a #
#   symbol. The disadvantage is that you have to do some work to pull out the
#   component values if you want to work with them individually.

#   A string is really a list of characters, so slice notation works on strings
#   just like it does on lists. 

#   Pick a color you like, and assign it to a variable as a hexadecimal string.
#   Using slices, print the red, green, and blue components of the color.

hexadecimal_color = '#eb3483'

#   Photo Filter 5-1: Clipped Reds
#   Every component of a color has a maximum value. In a 0-255 representation,
#   this is 255. Values greater than 255 may be rendered as if they were 255, or
#   they may cause an error, depending on how the image processing software was
#   written. It’s a good idea to manage component values yourself, so you are
#   handling out-of-bounds values in exactly the way that you want.

#   Start with Challenge 4-4, Bumped Reds. Modify your code in a way that if the
#   new red component has a value greater than the maximum legal value, it is
#   reset to match the maximum value. For example if the original red value is
#   245 and you multiply by 1.1, you would get 269.5. This is beyond the 255
#   maximum, so the red value should be set to 255.

#   Print your original color, and your modified color. Make sure you start with
#   a color that tests your error-checking code, such as [254, 200, 200].


initial_color = [254, 255, 100]

new_color = initial_color[:]

if new_color[0]*3 > 255:
    new_color[0] = 255
else:
    new_color[0] = new_color[0]*3


print("\nHere is my initial color:")
for value in initial_color:
    print(f"\t{value}")


print("\nHere is my new color with a red value brightened by a factor of 3:")
for value in new_color:
    print(f"\t{value}")


#   Photo Filter 5-2: Bounds Checking
#   Store component values in a list, but make sure one or two of the component
#   values are larger than they should be. For example, store a value greater
#   than 255 if you’re using the 0-255 model, or greater than 1 if you’re using
#   the 0-1 model.

#   Create a new, empty list called new_color. Loop through the components of
#   your original color, and add each component to new_color. However, if any
#   component is too high, store the maximum legal value for that component
#   instead of the original value.

#   Print the original color, and the new color.

boundcheck_color = [300, 100, 900]
print("\nHere is my original color:")
for value in boundcheck_color:
    print(f"\t{value}")

new_color = []

for value in boundcheck_color:
    if value > 255:
        new_color.append(255)
    else:
        new_color.append(value)

print("\nHere is my new color:")
for value in new_color:
    print(f"\t{value}")

#   As a list comprehension: 

new_color_list_comprehension = [value if value < 255 else 255 for value in boundcheck_color]

print("\nHere is my new color from the list comprehension:")
for value in new_color_list_comprehension:
    print(f"\t{value}")


