# Write a function which generates a six digit/character random_user_id
import random


def random_user_id():
    s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    res = ''
    for i in range(6):
        res += random.choice(s)
    return res                       
print(random_user_id())                # print(random_user_id());
print(" ")

# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    n = int(input("Enter n : "))
    t = int(input("Enter t : "))
    s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for i in range(t):
        res = ''
        for j in range(n):
            res += random.choice(s)
        print(res)

print(user_id_gen_by_user())
print(" ")

# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    n = random.randint(0, 10)
    lst = []
    for i in range(n):
        r = random.randint(0, 256)
        b = random.randint(0, 256)
        g = random.randint(0, 256)
        lst.append(f"rgb({r},{b},{g})")
    return lst
print(rgb_color_gen())
print(" ")

#
def generate_colors(type, n):
    if type == 'hexa':
        s = "0123456789abcdef"
        lst = []
        for i in range(n):
            res = '#'
            for j in range(6):
                res += random.choice(s)
            lst.append(res)
        print(lst)
    elif type == 'rgb':
        lst = []
        for i in range(n):
            r = random.randint(0, 256)
            b = random.randint(0, 256)
            g = random.randint(0, 256)
            lst.append(f"rgb({r},{b},{g})")
        print(lst)
    else:
        print("Enter type correctly")
print(generate_colors(12, 32))