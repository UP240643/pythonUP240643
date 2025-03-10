# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'
first_string = 'thirty'
second_string = 'days'
thirth_string = 'of'
fourth_string = "python"
space = ' '
concatenate = first_string + space + second_string + space + thirth_string + space + fourth_string

print(concatenate)

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'
first_string_2 = 'Coding'
second_string_2 = 'For'
thirth_string_2 = 'All'
space_2 = ' '
concatenate_2 = first_string_2 + space_2 + second_string_2 + space_2 + thirth_string_2

print(concatenate_2)

# Declare a variable named company and assign it to an initial value "Coding For All"
company = "Coding For All"

# Print the variable company using print()
print(company)

# Print the length of the company string using len() method and print()
print(len(company))

# Change all the characters to uppercase letters using upper() method
word = "epicamente"
print(word.upper())

# Change all the characters to lowercase letters using lower() method
word_2 = "LENTAMENTE"
print(word_2.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All
X = "Coding For All"
Y = "Coding For All"
z = "Coding For All"
print(X.capitalize())
print(Y.title())
print(z.swapcase())

# Cut(slice) out the first word of Coding For All string
W = "Coding For All"
print(slice("Coding"))

# Check if Coding For All string contains a word Coding using the method index, find or other methods
findindex = "Coding For All"
print(findindex.index("Coding For All"))


# Replace the word coding in the string 'Coding For All' to Python
remplace = "coding for all"
print(remplace.replace("coding" , "python"))

# Change Python for Everyone to Python for All using the replace method or other methods
remplace_2 = "Python for Everyone"
print(remplace_2.replace("Python for Everyone", "Python For All"))

# Split the string 'Coding For All' using space as the separator (split()) 
splite = "Coding For All"
print(splite.split())

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma
A = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(A.split(","))

# What is the character at index 0 in the string Coding For All
B = "Coding For All"
print(B.index("Coding For All"))

# What is the last index of the string Coding For All
C = "Coding For All"
print(C.index(C))

# What character is at index 10 in "Coding For All" string
D = "Coding For All"
print(C.index(" All", 10))

# Create an acronym or an abbreviation for the name 'Python For Everyone'
E = "Python For Everyone"
abbreviation = E[0:6]
print(abbreviation)

# Create an acronym or an abbreviation for the name 'Coding For All'
F = "Coding For All"
acronym = F[0:6:1]
print(acronym)

# Use index to determine the position of the first occurrence of C in Coding For All
G = "Coding For All"
print(G.index("C"))

# Use index to determine the position of the first occurrence of F in Coding For All
H = "Coding For All"
print(H.index("F"))

# Use rfind to determine the position of the last occurrence of l in Coding For All People
I = "Coding For All People"
print(I.rfind("l"))

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
J = 'You cannot end a sentence with because because because is a conjunction'
print(J.find("because"))

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
P = 'You cannot end a sentence with because because because is a conjunction'
print(J.find("because"))

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
QUE = 'You cannot end a sentence with because because because is a conjunction'
print(QUE.replace("because", ""))

# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
R = 'You cannot end a sentence with because because because is a conjunction'
print(R.index("because"))

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
WHAT = 'You cannot end a sentence with because because because is a conjunction'
print(WHAT.replace("because", ""))

# Does ''Coding For All' start with a substring Coding?
T = 'Coding For All'
print(T.startswith('Coding'))

# Does 'Coding For All' end with a substring coding?
S = 'Coding For All'
print(S.endswith('Coding'))

# '   Coding For All      '  , remove the left and right trailing spaces in the given string
ASARK = "   Coding For All      "
print(ASARK.replace(" ", ""))

#Which one of the following variables return True when we use the method isidentifier():
prhase = "30DaysOfPython"                  #30DaysOfPython                      
prhase_2 = "thirty_days_of_python"         #thirty_days_of_python                      
print(prhase.isidentifier())
print(prhase_2.isidentifier())

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string
library = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
union = ' #'.join(library)
print(union)

# Use the new line escape sequence to separate the following sentences
sentences =  'I am enjoying this challenge\nI just wonder what is next.'      # I am enjoying this challenge.
print(sentences)                                                              # I just wonder what is next.

# Use a tab escape sequence to write the following lines
print('Name\tAge\tCountry\tCity')                                   # Name      Age     Country   City
print('Asabeneh\t250\tFinland\tHelsinki')                           # Asabeneh  250     Finland   Helsinki

# Make the following using string formatting methods  
a = 8                                                 
b = 6                                                 
print(f'{a} + {b} = {a +b}')                                # 8 + 6 = 14
print(f'{a} - {b} = {a - b}')                               # 8 - 6 = 2
print(f'{a} * {b} = {a * b}')                               # 8 * 6 = 48
print(f'{a} / {b} = {a / b:.2f}')                           # 8 / 6 = 1.33
print(f'{a} % {b} = {a % b}')                               # 8 % 6 = 2
print(f'{a} // {b} = {a // b}')                             # 8 // 6 = 1
print(f'{a} ** {b} = {a ** b}')                             # 8 ** 6 = 262144                                                              
print("")                                          
                                                                    
                                                                        
                                                                        
                                                                       
                                                                        