# Iterate 0 to 10 using for loop, do the same using while loop.
contador = 0
while contador < 11:
    print(contador)
    contador = contador + 1
print(" ")

# Iterate 10 to 0 using for loop, do the same using while loop.
contador_invertido = 10
while contador_invertido > 0:
    print(contador_invertido)
    contador_invertido = contador_invertido - 1
print(" ")

# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
#
##
###
####
#####
######
#######

numbers = ("#", "##", "###", "####", "#####", "######", "#######",)
for number in numbers:
    print(number)
print(" ")

# Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
variable = {
    'skills': ['# # # # # # # #', '# # # # # # # #', '# # # # # # # #', '# # # # # # # #', '# # # # # # # #', '# # # # # # # #', '# # # # # # # #', '# # # # # # # #' ]

}
for key in variable:
    if key == 'skills':
        for skill in variable["skills"]:
            print(skill)
print(" ")

# Print the following pattern:
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100
person = {
    "0 x 0 = 0",
    "1 x 1 = 1",
    "2 x 2 = 4", 
    "3 x 3 = 9", 
    "4 x 4 = 16",
    "5 x 5 = 25",
    "6 x 6 = 36",
    "7 x 7 = 49", 
    "8 x 8 = 64",
    "9 x 9 = 81",
    "10 x 10 = 100"
    }

for number in person:
    print(number)
