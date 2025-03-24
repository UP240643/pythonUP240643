# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
for num in range(0, 101):
    print(num)
print("The sum of all numbers is ",sum (range(0, 101)))  # The sum of all numbers is 5050.
print(" ")

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
result = 0 
 
i = 2 
while i <= 100 : 
  if i % 2 == 0: 
    result = result + i 
  i += 2 
print("The sum of all even numbers is ", result) # The sum of all evens is 2550.
print(" ")

result = 0 
 
i = 1
while i <= 100 : 
  if i % 1 == 0: 
    result = result + i 
  i += 2
print("The sum of all odd numbers is ", result) # And the sum of all odds is 2500.
print(" ")



