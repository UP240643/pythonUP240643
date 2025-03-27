# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
print(" ")
def add_two_numbers ():
    first_num = 1121223
    last_num = 980735
    total = first_num + last_num
    print("la suma del numero", first_num, "y", last_num, "es", total)
add_two_numbers()
print(" ")

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_de_un_circulo (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print("el area de un circulo de radio", (17), "es", area_de_un_circulo(17))
print(" ")

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    total = 0
    for num in nums:
        total += num   
    return total
print(add_all_nums(12, 11, 8))
print(" ")

# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(C):
    F = C * 9 / 5 + 32
    return F
print("de", (12), "grados celcius es igual a", convert_celsius_to_fahrenheit(12), "grados farenheit")
print(" ")

# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month_1_3, month_4_6, month_7_9, month_10_12):
    autumn = "autumn = month", month_1_3,
    winter = "winter = month" ,month_10_12
    spring = "spring = month" ,month_7_9
    summer = "summer = month", month_4_6
    return autumn, winter, spring, summer
print(check_season(2, 5, 7, 10))
print(" ")

# Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(n):
    linear_ecuation = n + 2 * n
    return linear_ecuation
print(calculate_slope(12))
print(" ")

# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
from math import sqrt
A = int(input("Ingrese el coeficiente de la variable cuadrática "))
B = int(input("Ingrese el coeficiente de la variable lineal "))
C = int(input("Ingrese el término independiente "))
x1= 0
x2= 0
if ((B**2)-4*A*C) < 0:
  print("La solución de la ecuación es con números complejos")
else:
  x1 = (-B+sqrt(B**2-(4*A*C)))/(2*A)
  x2 = (-B-sqrt(B**2-(4*A*C)))/(2*A)
  print("Las soluciones de la ecuación son:")
  print(x1)
  print(x2)
print(" ")

# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list():
    list = ["frutas", "verduras", "carne", "huevos"]
    return list
print(print_list())
print(" ")

# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(lst):
    new_lst = []
    for i in range(-1, -(len(lst))-1, -1):
        new_lst.append(lst[i])
    return new_lst


print(reverse_list([1, 2, 3, 4]))
print(" ")


# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def new_capitalize_list_items(lst):
    lisst = []
    for item in lst:
        lisst.append(item.capitalize())
    return lisst
print(new_capitalize_list_items(["deeeam", "booooy"]))
print(" ")

# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_items(lst, item):
    lst.append(item)
    return lst

numbers = [1, 2, 4, 3, 6]
print(add_items(numbers, 5))
print(" ")

# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(lst, item):
    lst.remove(item)
    return(lst)

items = ["porque", "me", "eliminas", "brou"]
print(remove_item(items, "me"))
print(" ")

# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(num):
    sum = 0
    for i in range(num+1):
        sum += 1
    return sum
print(sum_of_numbers(3))
print(" ")

# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(num):
    sum = 0
    for i in range(num+1):
        if i % 2 != 0:
            sum += i
    return sum

print(sum_of_odds(9))
print(" ")

# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_numbers(num):
    sum = 0
    for i in range(num+1):
        if i % 2 == 0:
            sum += i
    return sum

print(sum_of_numbers(12))
print(" ")
