print ("Ejemplo #1")
# Almacena el actual número más grande aquí.
largest_number = -999999999

# Ingresa el primer valor.
number = int(input("Introduce un número o escribe -1 para detener: "))

# Si el número no es igual a -1, continuaremos
while number != -1:
    # ¿Es el número más grande que el valor de largest_number?
    if number > largest_number:
        # Sí si, se actualiza largest_number.
        largest_number = number
    # Ingresa el siguiente número.
    number = int(input("Introduce un número o escribe -1 para detener: "))

# Imprime el número más grande
print("El número más grande es:", largest_number, "\n")

print("Ejemplo #2")
# Un programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares.
# El programa termina cuando se ingresa un cero.

odd_numbers = 0
even_numbers = 0

# Lee el primer número.
number = int(input("Introduce un número o escribe 0 para detener: "))

# 0 termina la ejecución.
while number != 0:
    # Verificar si el número es impar.
    if number % 2 == 1:
        # Incrementar el contador de números impares odd_numbers.
        odd_numbers += 1
    else:
        # Incrementar el contador de números pares even_numbers.
        even_numbers += 1
    # Leer el siguiente número.
    number = int(input("Introduce un número o escribe 0 para detener: "))

# Imprimir resultados.
print("Cuenta de números impares:", odd_numbers)
print("Cuenta de números pares:", even_numbers, "\n")

'''Ciertas expresiones se pueden simplificar sin cambiar el comportamiento del programa.

Intenta recordar cómo Python interpreta la verdad de una condición y ten en cuenta que 
estas dos formas son equivalentes:

while number != 0: y while number:

La condición que verifica si un número es impar también puede codificarse en estas 
formas equivalentes:

if number % 2 == 1: y if number % 2:'''

print("Ejemplo #3 - counter para salir del bucle")
counter = 5
while counter != 0:
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)

print("Forma más compacta del mismo codigo")
counter = 5
while counter:
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)


