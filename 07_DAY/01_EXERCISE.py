# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
print(len(it_companies))

# Add 'Twitter' to it_companies
print(" ")
it_companies.add("Twitter")
print(it_companies)

# Insert multiple IT companies at once to the set it_companies
print(" ")
it_companies.update(["YouTube", "WhatsApp", "TNT"])
print(it_companies)

# Remove one of the companies from the set it_companies
print(" ")
it_companies.remove("IBM")
print(it_companies)

# What is the difference between remove and discard
print(" ")
it_companies.discard("WhatsApp")
print(it_companies)
print(" ")