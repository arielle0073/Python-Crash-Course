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

#   avg_gray: Find the average of the three RGB values, and use this value for
#   all three RGB values of the new color.


#   max_gray: Find the maximum of the three RGB values, and use this value for
#   all three RGB values of the new color.

#   min_gray: Find the minimum of the three RGB values, and use this value for
#   all three RGB values of the new color.

#   r_gray: Use the red component of the original color as the value for all
#   three RGB values of the new color.

#   Print your original color, and each shade of gray based on that color.
