# Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
positive_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print("positive numbers: ", (positive_numbers))                
print(" ")

# Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten_list = [number for row in list_of_lists for number in row]
print("flatten list: ", (flatten_list))
print(" ")

# Using list comprehension create the following list of tuples:
list = [(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]
result = [(i, 1, i * 1, i ** 2, i ** 3, i ** 4, i ** 5) for i in range(11)]

print("result: ", result)
print(" ")

# Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flatten_countries = [str for row in countries for str in row ]
print("flatten countries: ", (flatten_countries))
print(" ")

# Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries_dict = [{'country': country, 'capital': capital} for dict in countries for country, capital in dict]
print("countries diccionary: ", countries_dict)
print(" ")

# Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
countries_concatenated = [f"{first} {last}" for sublist in names for first, last in sublist]
print("countries concatenated", countries_concatenated)
print(" ")

# Write a lambda function which can solve a slope or y-intercept of linear functions.
calculate_slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else None
calculate_y_intercept = lambda x1, y1, slope: y1 - slope * x1 if slope is not None else None
x1, y1 = 2, 3
x2, y2 = 5, 11

slope = calculate_slope(x1, y1, x2, y2)
print("Slope: ", slope)  

y_intercept = calculate_y_intercept(x1, y1, slope)
print("Y-Intercept: ", y_intercept)  