# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(num):
    ecount = 0
    ocount = 0
    for i in range(num+1):
        if i % 2 == 0:
            ecount += 1
        else:
            ocount += 1
    print(f"The number of odds are {ocount}.")
    print(f"The number of evenss are {ecount}.")


evens_and_odds(100)
print(" ")

# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    return fact


print(factorial(5))

# Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(o):
     if len(o):
        print("Not Empty")
     else:
        print("Empty")

# Write ddef unique(lst):
def unique(lst):
    for i in lst:
        for j in range(i, len(lst)):
            if i == lst[j]:
                return "Not Unique"
    return "Unique"


print(unique([1, 2, 3, 4]))


def same_type(lst):
    for i in lst:
        for j in range(i, len(lst)):
            if type(i) != type(lst[j]):
                return "Not Same"
    return "Same"


print(same_type([1, 2, 3, 4]))
