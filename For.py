#Bucles en tu código con for
for i in range(100):
    # do_something()
    print(i)
    pass
print("\n")
'''
Existen algunos elementos nuevos. Déjanos contarte sobre ellos:

-La palabra reservada for abre el bucle for; nota - No hay condición después de eso; 
no tienes que pensar en las condiciones, ya que se verifican internamente, sin ninguna intervención.
-Cualquier variable después de la palabra reservada for es la variable de control del bucle; 
cuenta los giros del bucle y lo hace automáticamente.
-La palabra reservada in introduce un elemento de sintaxis que describe el rango de valores posibles 
que se asignan a la variable de control.
-La función range() (esta es una función muy especial) es responsable de generar todos los valores 
deseados de la variable de control; en nuestro ejemplo, la función creará (incluso podemos decir que 
alimentará el bucle con) valores subsiguientes del siguiente conjunto: 0, 1, 2 .. 97, 98, 99; nota: 
en este caso, la función range() comienza su trabajo desde 0 y lo finaliza un paso (un número entero) 
antes del valor de su argumento.
-Nota la palabra clave pass dentro del cuerpo del bucle - no hace nada en absoluto; es una instrucción vacía : 
la colocamos aquí porque la sintaxis del bucle for exige al menos una instrucción dentro del cuerpo 
(por cierto, if, elif, else y while expresan lo mismo).
'''
print("Función range con 1 argumento")
for i in range(10):
    print("El valor de a es actualmente", i)
    pass
print ("\n")
''' Nota:
El bucle se ha ejecutado diez veces (es el argumento de la función range()).
El valor de la última variable de control es 9 (no 10, ya que comienza desde 0 , no desde 1). '''
#La invocación de la función range() puede estar equipada con dos argumentos, no solo uno:
print("Función range con 2 argumentos")
for i in range(2, 8):
    print("El valor de i es actualmente", i)
    pass
print ("\n")
'''En este caso, el primer argumento determina el valor inicial (primero) de la variable de control.
El último argumento muestra el primer valor que no se asignará a la variable de control.
Nota: la función range() solo acepta enteros como argumentos y genera secuencias de enteros.
¿Puedes adivinar la salida del programa? Ejecútalo para comprobar si ahora también estabas en lo cierto.
El primer valor mostrado es 2 (tomado del primer argumento de range()).
El último es 7 (aunque el segundo argumento de range() es 8).'''

#La función range() con tres argumentos
print("Función range con 3 argumentos")
for i in range(2, 8, 3):
    print("El valor de i es actualmente", i)

print ("\n")
'''El tercer argumento es un incremento: es un valor agregado para controlar la variable en cada 
giro del bucle (como puedes sospechar, el valor predeterminado del incremento es 1).

¿Sabes por qué? El primer argumento pasado a la función range() nos dice cual es el número de inicio 
de la secuencia (por lo tanto, 2 en la salida). El segundo argumento le dice a la función dónde detener 
la secuencia (la función genera números hasta el número indicado por el segundo argumento, pero no lo incluye). 
Finalmente, el tercer argumento indica el paso, que en realidad significa la diferencia entre cada número 
en la secuencia de números generados por la función.

2 (número inicial) → 5 (2 incremento por 3 es igual a 5 - el número está dentro del rango de 2 a 8) → 8 
(5 incremento por 3 es igual a 8 - el número no está dentro del rango de 2 a 8, porque el parámetro de parada 
no está incluido en la secuencia de números generados por la función).

'''

#Nota: si el conjunto generado por la función range() está vacío, el bucle no ejecutará su cuerpo en absoluto.
#Al igual que aquí, no habrá salida:

for i in range(1, 1):
    print("El valor de i es actualmente", i)

#Nota: el conjunto generado por range() debe ordenarse en un orden ascendente. 
#No hay forma de forzar el range() para crear un conjunto en una forma diferente. 
#Esto significa que el segundo argumento de range() debe ser mayor que el primero.
#Por lo tanto, tampoco habrá salida aquí:
    
for i in range(2, 1):
    print("El valor de i es actualmente", i)

#Echemos un vistazo a un programa corto cuya tarea es escribir algunas de las primeras potencias de dos:

power = 1
for expo in range(16):
    print("2 a la potencia de", expo, "es", power)
    power *= 2
print("\n")

'''La variable expo se utiliza como una variable de control para el bucle e indica el valor actual del exponente. 
La propia exponenciación se sustituye multiplicando por dos. Dado que 2 0 es igual a 1, después 2 × 1 es igual a 21, 
2 × 21 es igual a 22, y así sucesivamente.'''