# Declara 5 como num_uno y 4 como num_dos
num_1 = 5
num_2 = 4
total = num_1 + num_2   # Suma num_uno y num_dos y asigna el valor a una variable total
diff = num_1 - num_2   # Restar num_dos de num_uno y asignar el valor a una variable diff
product = num_2 * num_1   # Multiplicar numero_dos por numero_uno y asignar el valor a una variable producto
division = num_1 / num_2   # Divide num_uno entre num_dos y asigna el valor a una variable división
remainder = num_1 % num_2   #Utilizar la división módulo para hallar num_dos dividido por num_uno y asignar el valor a una variable remainder
floor_division = num_1 // num_2   # Halla floor división de num_uno entre num_dos y asigna el valor a una variable floor_division
exponential = num_2 ** num_1   # Calcular num_uno a la potencia de num_dos y asignar el valor a una variable exp

# Comprueba el tipo de datos de todas tus variables utilizando la función incorporada type()
print(type(num_1))
print(type(num_2))
print(type(total))
print(type(diff))
print(type(product))
print(type(division))
print(type(remainder))
print(type(floor_division))
print(type(exponential))

# Utiliza la función len() para averiguar la longitud de tu nombre.
len("Hugo Eduardo Almaguer Navarro") 

# Compara la longitud de tu nombre y tu apellido
print(len('EDUARDO') == len('ALMAGUER')) 

print(' num_1 + num_2 =', total)  
print('num_1 - num_2 = ', diff)   
print('num_2 * num_1 = ', product)   
print('num_1 / num_2 = ', division)  
print('num_1 % num_2 = ', remainder)   
print('num_1 // num_2 = ', floor_division)   
print('num_2 ** num_1 = ', exponential)   


# El radio de un círculo es de 30 metros.
radio = int(input("radio = "))   # Tome el radio como entrada del usuario y calcule el área.
area_de_un_circulo = 3.14 * radio ** 2   # Calcular el área de un círculo y asignar el valor a una variable de nombre area_del_circulo     
circunferencia_de_un_circulo =  2 * radio   #Calcula la circunferencia de un círculo y asigna el valor a una variable de nombre circunferencia_de_un_circulo
print('El area del circulo es... ', area_de_un_circulo) 
print('La circunferencia del circulo es... ', circunferencia_de_un_circulo) 

# Utilizar la función de entrada incorporada para obtener el nombre, apellido, país y edad de un usuario y almacenar el valor
nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
ciudad = input("Introduce tu cuidad: ")
edad = input("Introduce tu edad: ")

print("hola",nombre, apellido, "tienes", edad)

# Ejecute help('keywords') en el shell de Python o en su archivo para comprobar las palabras reservadas o palabras clave de Python
help("keywords")