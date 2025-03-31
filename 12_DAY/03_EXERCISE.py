# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
import random

def shuffle_list(input_list):
    shuffled = input_list[:]  
    random.shuffle(shuffled)  
    return shuffled

original_list = [1, 2, 3, 4, 5]
shuffled_list = shuffle_list(original_list)

print("original list:", original_list)  
print("shuffled list:", shuffled_list) 
print(" ")

# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def random_numbers():
    return random.sample(range(10), 7)

print(random_numbers())
