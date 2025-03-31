import keyword
from collections import Counter
from countries_data import countries_d 

# Write a function called is_prime, which checks if a number is prime.
def is_prime(number):
    if number <= 1:
        return False 
    for i in range(2, int(number**0.5) + 1):  
        if number % i == 0:
            return False  
    return True  
print(is_prime(1234))  
print(is_prime(37)) 
print(" ")

# Write a functions which checks if all items are unique in the list.
def all_items_unique(input_list):
    return len(input_list) == len(set(input_list))
print(all_items_unique([1, 2, 3, 4]))  
print(all_items_unique([1, 2, 2, 4]))  
print(" ")

# Write a function which checks if all the items of the list are of the same data type.
def all_same_type(input_list):
    if not input_list:
        return True  
    first_type = type(input_list[0])  
    return all(isinstance(item, first_type) for item in input_list)

print(all_same_type([8, 4, 3, 1]))  
print(all_same_type(["w", "q", "x"]))  
print(all_same_type([1111, "b", 88]))  
print(" ")

# Write a function which check if provided variable is a valid python variable

def valid_variable(variable_name):
    if not variable_name:
        return False
    if variable_name[0].isdigit():
        return False
    if not variable_name.isidentifier():
        return False
    if keyword.iskeyword(variable_name):
        return False
    return True

print(valid_variable("my_var"))  
print(valid_variable("2nd_var")) 
print(valid_variable("for")) 
print(valid_variable(""))  

# Go to the data folder and access the countries-data.py file.
# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
def most_spoken_languages(n=10):
    language_counter = Counter()
    
    for country in countries_d:
        for language in country['languages']:
            language_counter[language] += 1

    return language_counter.most_common(n)

def most_populated_countries(n=10):
    sorted_countries = sorted(countries_d, key=lambda x: x['population'], reverse=True)
    return [(country['name'], country['population']) for country in sorted_countries[:n]]
print(most_spoken_languages(20))
print(most_populated_countries(20))