# Declare an empty list
empty_list = list()
print(len(empty_list))
      
# Declare a list with more than 5 items
list = ["youtube", "damian", "macizo", "perlas", "nicotina", "xd"]
print(list)

# Find the length of your list
print(len(list))

# Get the first item, the middle item and the last item of the list
print(list[0])
print(list[3])
print(list[5])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_types = ["Eduardo", "18", "63.4", "single", "20303"]

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print("number of companies:", len(it_companies))

# Print the first, middle and last company
print("First company: ", it_companies[0])
print("Middle company: ", it_companies[3])
print("Last company: ", it_companies[6])

# Print the list after modifying one of the companies
it_companies[0] = "Reddit"
print(it_companies)

# Add an IT company to it_companies
it_companies.append("Twitter")
print(it_companies)

# Insert an IT company in the middle of the companies list
it_companies.insert(4, "JBL")
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
print(it_companies[2].upper())

# Join the it_companies with a string '#;  '
it_str = "#; ".join(it_companies)
print(it_str)

# Check if a certain company exists in the it_companies list.
does_exist = "Microsoft" in it_companies
print(does_exist)

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list
first_three_companies = it_companies[3:9] 
print(first_three_companies)

# Slice out the last 3 companies from the list
last_three_companies = it_companies[0:6]
print(last_three_companies)

# Slice out the middle IT company or companies from the list
del it_companies [1]
print(it_companies)

# Remove the first IT company from the list
del it_companies[0]
print(it_companies)

# Remove the middle IT company or companies from the list
del it_companies[4]
print(it_companies)

# Remove the last IT company from the list
del it_companies[5]

# Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# Destroy the IT companies list
del it_companies

# Join the following lists:
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end =['Node','Express', 'MongoDB']
print(front_end)
print(back_end)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
join_stack = front_end + back_end
print(join_stack)

full_stack = join_stack.copy()
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")
print(full_stack)
print("")
