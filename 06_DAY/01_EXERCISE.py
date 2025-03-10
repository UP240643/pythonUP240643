# Create an empty tuple
empty_tuple = tuple()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
names_tuple = ("Marian", "Rebbeca", "Main", "Kiwi")
print("Names: ", names_tuple)
print("Total names: ", len(names_tuple))

# Join brothers and sisters tuples and assign it to siblings
brothers = ("Main", "David", "Tanaka", "Adam Smasher")
sisters = ("Marian", "Rebbeca", "Kiwi")
siblings = brothers + sisters
print("MY FAMILY")
print("")
print("Brothers: ", brothers)
print("Sisters: ", sisters)
print("Siblings: ", siblings)

# How many siblings do you have?
print("")
print("I have ",len(siblings), "siblings")

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
Parents = ("Walter White", "Rita Morgan")
Family_members = Parents + siblings
print("")
print("Siblings and Parents: ", Family_members)