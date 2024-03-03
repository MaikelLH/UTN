#Ejemplo 1: 
#Se leen dos números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))

# Elige el número más grande
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# Imprime el resultado
print("El número más grande es:", larger_number)

'''El fragmento de código anterior debe estar claro: 
lee dos valores enteros, los compara y encuentra cuál es el más grande.'''

#Ejemplo 2:
'''Ahora vamos a mostrarte un hecho intrigante. Python tiene una 
característica interesante, mira el código a continuación:'''

#Se leen dos números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))

# Elige el número más grande
if number1 > number2: larger_number = number1
else: larger_number = number2

# Imprime el resultado
print("El número más grande es:", larger_number)

'''Nota: si alguna de las ramas de if-elif-else contiene una sola instrucción, 
puedes codificarla de forma más completa (no es necesario que aparezca una 
línea con sangría después de la palabra clave), pero solo continúa la línea 
después de los dos puntos).

Sin embargo, este estilo puede ser engañoso, y no lo vamos a usar en nuestros 
programas futuros, pero definitivamente vale la pena saber si quieres leer y 
entender los programas de otra persona.

No hay otras diferencias en el código.'''

# Ejemplo 3:

'''Es hora de complicar el código: encontremos el mayor de los tres números. 
¿Se ampliará el código? Un poco.

Suponemos que el primer valor es el más grande. Luego verificamos esta 
hipótesis con los dos valores restantes.'''

# Se leen tres números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))

# Asumimos temporalmente que el primer número
# es el más grande.
# Lo verificaremos pronto.
largest_number = number1

# Comprobamos si el segundo número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario.
if number2 > largest_number:
    largest_number = number2

# Comprobamos si el tercer número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario.
if number3 > largest_number:
    largest_number = number3

# Imprime el resultado.
print("El número más grande es:", largest_number)

'''Este método es significativamente más simple que tratar de encontrar 
el número más grande comparando todos los pares de números posibles 
(es decir, el primero con el segundo, el segundo con el tercero y 
el tercero con el primero)'''
