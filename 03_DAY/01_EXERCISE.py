age = int(10) #Declare your age as integer variable
height = 1.76 #Declare your height as a float variable
comp = 25j   #Declare a variable that store a complex number
print(age)   
print(height)
print(comp)

#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
b = int(input('base = '))
h = int(input('height = '))
print('The area is = ', 0.5*b*h)

#Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = int(input('Side a = '))
side_b = int(input('Side b = '))
side_c = int(input('Side c = '))
perimeter = side_a + side_b + side_c
print('The perimeter equals', perimeter)

#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = int(input('length = '))
width = int(input('width = '))
area_rec, perimeter_rec = width*length, 2*(length + width)
print('area is', area_rec, 'perimeter is', perimeter_rec)

#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = int(input('radius= '))
pi = 3.14
area_circ, circum = pi*radius**2, 2*pi*radius
print('area is', area_circ, 'circumference is', circum)

#Calculate the slope, x-intercept and y-intercept of y = 2x -2
x = int(input('x= '))
slope = (2*x)-2
print(slope)

#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
slope1 = (10-2)/(6-2)
print(slope1)

#Compare the slopes in tasks 8 and 9.
x = int(input('x= '))

#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
y = (x**2)+(6*x)+9
print(y)

#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len('python') < len('dragon'))

#Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jargon' in 'i hope this course is not full of jargon')

#There is no 'on' in both dragon and python
print('on' not in 'python' and 'on' not in 'dragon')

#Find the length of the text python and convert the value to float and convert it to string
print(len('python'))
print(float(len('python')))
print(str(len('python')))

#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
num = int(input ('Enter any number: ')) 
if((num % 2) == 0): print('even') 
else: print('The provided number is odd')

#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7//3 == 2.7)

#Check if type of '10' is equal to type of 10
print('10' == 10)

#Check if int('9.8') is equal to 10
print(9.8 == 10)

#Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hrs = int(input('hours: '))
rate = int(input('rate: '))
pay = hrs * rate 
print('payment: ',pay)

#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input('Number of years: '))
seconds = years*3600 
print('youve lived for: ', seconds)

#Write a Python script that displays the following table
for i in range(1,6):
    print(f'{i} {i**0} {i**2} {i**3}')
print("")