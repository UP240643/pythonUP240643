# Write a code which gives grade to students according to theirs scores:      
# 80-100, A
# 70-89, B
#60-69, C
# 50-59, D
# 0-49, F
score = int(input("Enter your score: "))
if 80 <= score <= 100:
    print("Grado: A")
elif 70 <= score <= 89:
    print("Grado: B")
elif 60 <= score <= 69:
    print("Grado: C")
elif 50 <= score <= 59:
    print("Grado: D")
else:
    print("Grado: F")

# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
month = input("Enter a month: ").lower()
if month in ['september', 'october', 'november']:
    print("Season: Autumn")
    print(" ") 
elif month in ['december', 'january', 'february']:
    print("Season: Winter")
    print(" ") 
elif month in ['march', 'april', 'may']:
    print("Season: Spring")
    print(" ") 
elif month in ['june', 'july', 'august']:
    print("Season: Summer")
    print(" ") 
else:
    print("Invalid month")
    print(" ") 

# ```sh
# fruits = ['banana', 'orange', 'mango', 'lemon']
# ```

#If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
# The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruits = input("Enter a fruit: ").lower()

if (new_fruits in fruits):
    print("That fruit already exists in the list")
else:
    fruits.append(new_fruits)
    print("Modified fruit list:", fruits)






