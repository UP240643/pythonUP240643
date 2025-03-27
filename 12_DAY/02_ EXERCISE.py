# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).  
import random 
import string

def list_of_hexa_colors():   
    num_colors = 6
    hex_colors = ['#' + ''.join(random.choices('0123456789abcdef', k=6)) for _ in range(num_colors)]
    return hex_colors

print(list_of_hexa_colors())
print(" ")

# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.  
def list_of_rgb_colors(num_colors):
    rgb_colors = []
    for _ in range(num_colors):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        rgb_colors.append(color)
    return rgb_colors


print(list_of_rgb_colors(6))  
print(" ")

# Write a function generate_colors which can generate any number of hexa or rgb colors.

# generate_colors('num_colors', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
# generate_colors('num_colors', 1) # ['#b334ef']
# generate_colors('color_type', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
# generate_colors('color_type', 1)  # ['rgb(33,79, 176)']