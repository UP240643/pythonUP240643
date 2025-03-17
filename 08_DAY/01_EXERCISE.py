# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog = {}
print(" ")
dog["name"] = "Cowboy"
dog["color"] = "black"
dog["breed"] = "Pastor Aleman"
dog["legs"] = "Triangular"
dog["age"] = "20 years"
print(dog)
print(" ")

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student_diccionary = {}
student_diccionary["first_name"] = "Hugo"
student_diccionary["last_name"] = "Almaguer"
student_diccionary["gender"] = "Male"
student_diccionary["marital_status"] = "single"
student_diccionary["skills"] = ["inteligent", "strong", "sabio"]
student_diccionary["country"] = "Mexico"
student_diccionary["city"] = "Aguascalientes"
student_diccionary["addres_as_key"] = "20432" 
print(student_diccionary)
print(" ")

# Get the length of the student dictionary
print(len(student_diccionary))
print(" ")

# Get the value of skills and check the data type, it should be a list
print(student_diccionary["skills"])
print(type(student_diccionary["skills"]))
print(" ")

# Modify the skills values by adding one or two skills
student_diccionary["skills"].append("Murder")
print(student_diccionary["skills"])
print(" ")

# Get the dictionary keys as a list
keys = student_diccionary.keys()
print(keys)
print(" ")

# Get the dictionary values as a list
values = student_diccionary.values()
print(values)
print(" ")

# Change the dictionary to a list of tuples using items() method
print(student_diccionary.items())
print(" ") 

# Delete one of the items in the dictionary
student_diccionary.pop("country")
print(student_diccionary)
print(" ") 

# Delete one of the dictionaries
del student_diccionary
