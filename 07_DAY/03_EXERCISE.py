# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
print(" ")
age = [22, 19, 24, 25, 26, 24, 25, 24]
ages = set(age)
print(len(ages))
print(len(age))

# Explain the difference between the following data types: string, list, tuple and set
set = {'item1', 'item2', 'item3', 'item4'} # Set is a collection of items
list = ['item1', 'item2', 'item3', 'item4'] # List is a collection which is ordered and changeable(modifiable)
tuple = ('item1', 'item2', 'item3', 'item4') # A tuple is a collection of different data types which is ordered and unchangeable (immutable)
string = "Deam" # Text is a string data type. Any data type written as text is a string.

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people."
print(sentence.split())