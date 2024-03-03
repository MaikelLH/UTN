#Ejercicio 1
print("Practica #1 - input")
#Escenario:
'''Espatifilo, más comúnmente conocida como la planta de cuna de Moisés o flor de la paz, 
es una de las plantas para interiores más populares que filtra las toxinas dañinas del aire. 
Algunas de las toxinas que neutraliza incluyen benceno, formaldehído y amoníaco.

Imagina que tu programa de computadora ama estas plantas. Cada vez que recibe una entrada 
en forma de la palabra Espatifilo, grita involuntariamente a la consola la siguiente cadena: 
"¡Espatifilo es la mejor planta de todas!"


Escribe un programa que utilice el concepto de ejecución condicional, 
tome una cadena como entrada y que:

-Imprima el enunciado "Si, ¡El ESPATIFILIO! es la mejor planta de todos los tiempos!" 
en la pantalla si la cadena ingresada es "ESPATIFILIO".
-Imprima "No, ¡quiero un gran ESPATIFILIO!" si la cadena ingresada es "espatifilo".
-Imprima "¡ESPATIFILIO!, ¡No [entrada]!" de lo contrario. Nota: [entrada] es la 
cadena que se toma como entrada.

Prueba tu código con los datos que te proporcionamos. ¡Y hazte de un ESPATIFILIO también!


Datos de Prueba
Entrada de muestra: espatifilo
Resultado esperado: No, ¡quiero un gran ESPATIFILIO!

Entrada de ejemplo: pelargonio
Resultado esperado: !ESPATIFILIO!, ¡No pelargonio!

Entrada de muestra: ESPATIFILIO
Resultado esperado: Si, ¡El ESPATIFILIO es la mejor planta de todos los tiempos!'''
print("Practica #1 - Usar input")
nombre_planta = input(str("Ingresa el nombre de la Planta: "))
if nombre_planta == "ESPATIFILIO":
    print("Si, ¡El ESPATIFILIO es la mejor planta de todos los tiempos!")
elif nombre_planta == "espatifilo":
    print("No, ¡quiero un gran ESPATIFILIO!")
else: print("¡ESPATIFILIO!, ¡ No",nombre_planta,"!\n")

#Ejercicio 2
print("Practica #2 - Usar if-else")
#Escenario:
'''Érase una vez una tierra de leche y miel, habitada por gente feliz y próspera. 
La gente pagaba impuestos, por supuesto, su felicidad tenía límites. El impuesto 
más importante, denominado Impuesto Personal de Ingresos (IPI, para abreviar) 
tenía que pagarse una vez al año y se evaluó utilizando la siguiente regla:

Si el ingreso del ciudadano no era superior a 85,528 pesos, el impuesto era igual 
al 18% del ingreso menos 556 pesos y 2 centavos (esta fue la llamada exención fiscal ).
Si el ingreso era superior a esta cantidad, el impuesto era igual a 14,839 pesos 
y 2 centavos, más el 32% del excedente sobre 85,528 pesos.

Tu tarea es escribir una calculadora de impuestos.

Debe aceptar un valor de punto flotante: el ingreso.
A continuación, debe imprimir el impuesto calculado, redondeado a pesos totales. 
Hay una función llamada round() que hará el redondeo por ti, la encontrarás en el 
código de esqueleto del editor.

Nota: Este país feliz nunca devuelve dinero a sus ciudadanos. Si el impuesto calculado 
es menor que cero, solo significa que no hay impuesto (el impuesto es igual a cero). 
Ten esto en cuenta durante tus cálculos.

Observa el código en el editor: solo lee un valor de entrada y genera un resultado, 
por lo que debes completarlo con algunos cálculos inteligentes.

Datos de Prueba
Entrada de muestra: 10000

Resultado esperado: El impuesto es: 1244.0 pesos

Entrada de muestra: 100000

Resultado esperado: El impuesto es: 19470.0 pesos

Entrada de muestra: 1000

Resultado esperado: El impuesto es: 0.0 pesos

Entrada de muestra: -100

Resultado esperado: El impuesto es: 0.0 pesos
'''

ingreso = float(input("Ingresa tu ingreso anual: "))

# Calcula el impuesto
if ingreso <= 85528:
    impuesto = ingreso * 0.18 - 556.02
else:
    impuesto = 14839.02 + (ingreso - 85528) * 0.32

# Redondea el impuesto a pesos totales
impuesto = round(impuesto)

# Si el impuesto es negativo, establece el impuesto en cero
if impuesto < 0:
    impuesto = 0

# Imprime el resultado
print(f"El impuesto es: {impuesto:.1f} pesos")

'''print(f"El impuesto es: {impuesto:.1f} pesos")
print: Esta es una función incorporada en Python que se utiliza para mostrar 
información en la consola o en la salida estándar.
f: Esto indica que estamos utilizando f-strings (cadenas formateadas). 
Las f-strings son una forma conveniente de formatear cadenas en Python, 
permitiéndonos insertar valores de variables dentro de una cadena.
"El impuesto es: {impuesto:.1f} pesos": Esta es la cadena que se imprimirá. 
Contiene un marcador de posición {impuesto:.1f}. Aquí está lo que significa 
cada parte:
{impuesto}: Esto es un marcador de posición para el valor de la variable impuesto.
:.1f: Esto es una especificación de formato. El :.1f significa que queremos 
formatear el valor de impuesto como un número de punto flotante con un decimal.
"pesos": Esto simplemente agrega la palabra “pesos” al final de la cadena.
En resumen, esta línea de código toma el valor de la variable impuesto, 
lo formatea como un número de punto flotante con un decimal y lo muestra junto 
con el texto “El impuesto es:”. Por ejemplo, si el impuesto calculado es 1244.0, 
la línea imprimirá “El impuesto es: 1244.0 pesos”.
'''


'''print ("PRIMER PRUEBA")
income = float(input("Introduce el ingreso anual: "))
if income < 85528.00:
    taxes = 18
    exención_fiscal = 556.02
    ipi = (((income * taxes/100)-exención_fiscal))
    tax = ipi <= 0

if income > 85528.00:
    taxes = 14839.02
    excedente = 32
    excedentes = 85528.00
    tax = ((((income - excedentes) * excedente/100)) + taxes)
else:
    if income <= 0:
        tax = income 
    else: 0
tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")

#prueba anidada
print ("SEGUNDA PRUEBA")
income = float(input("Introduce el ingreso anual:"))
if tax:
    if income >= 1 and income < 85528.00:
        taxes = 18
        exención_fiscal = 556.02
        tax = (income * taxes/100)-exención_fiscal
        tax <= 0 
    else: tax <= 0
else: 
    if income > 85528.00:
        taxes = 14839.02
        excedente = 32
        excedentes = 85528.00
        tax = ((((income - excedentes) * excedente/100)) + taxes)
    else: tax <= 0
    tax = 0

tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")

print ("TERCER PRUEBA")
income = float(input("Introduce el ingreso anual: "))
if income <= 0:
        tax = 0
elif income >= 1 and income <= 85528.00:
    taxes = 18
    exención_fiscal = 556.02
    tax = (income * taxes/100)-exención_fiscal
else:
    income >= 85528.00
    taxes = 14839.02
    excedente = 32
    excedentes = 85528.00
    tax = ((((income - excedentes) * excedente/100)) + taxes)
tax = round(tax, 0)
print("El impuesto es:", tax, "pesos\n")
print("Practica #3 - Usar if-elif-else")
print ("Primer PRUEBA")
'''
'''Escenario
Como seguramente sabrás, debido a algunas razones astronómicas, 
el año pueden ser bisiesto o común. Los primeros tienen una duración de 366 días, 
mientras que los últimos tienen una duración de 365 días.

Desde la introducción del calendario Gregoriano (en 1582), se utiliza la siguiente 
regla para determinar el tipo de año:

Si el número del año no es divisible entre cuatro, es un año común.
De lo contrario, si el número del año no es divisible entre 100, es un año bisiesto.
De lo contrario, si el número del año no es divisible entre 400, es un año común.
De lo contrario, es un año bisiesto.
Observa el código en el editor: solo lee un número de año y debe completarse con las 
instrucciones que implementan la prueba que acabamos de describir.

El código debe mostrar uno de los dos mensajes posibles, que son Año Bisiesto o Año Común, 
según el valor ingresado.

Sería bueno verificar si el año ingresado cae en la era Gregoriana y emitir una advertencia 
de lo contrario: No dentro del período del calendario Gregoriano. Consejo: utiliza los operadores != y %.

Prueba tu código con los datos que hemos proporcionado.

Datos de Prueba
Entrada de muestra: 2000

Resultado esperado: Año Bisiesto

Entrada de muestra: 2015

Resultado esperado: Año Común

Entrada de muestra: 1999

Resultado esperado: Año Común

Entrada de muestra: 1996

Resultado esperado: Año Bisiesto

Entrada de muestra: 1580

Resultado esperado: No esta dentro del período del calendario Gregoriano
'''
year = int(input("Introduce un año: "))
if year >= 1582 and year % 4 == 0:
     print("Año Común")
elif year >= 1582 and year % 100 != 0:
     print("Año Bisiesto")
elif year >= 1582 and year % 400 == 0:
     print ("OTRO Año Común")
else:
     print ("No dentro del período del Calendario Gregoriano\n")

#
# Escribe tu código aquí.
#
print ("Ejercicios de Resumen:\n\nEjercicio #1\n¿Cuál es la salida del siguiente fragmento de código?")
x = 5
y = 10
z = 8
print(x > y)
print(y > z,"\n")

print("Ejercicio #2\n¿Cuál es la salida del siguiente fragmento de código?")
x, y, z = 5, 10, 8
print(x > z)
print((y-5)==x, "\n")

print("Ejercicio #3\n¿Cuál es la salida del siguiente fragmento de código?")
x, y, z = 5, 10, 8
x, y, z = z, y, x
print(x > z)
print((y-5)==x, "\n")

print("Ejercicio #4\n¿Cuál es la salida del siguiente fragmento de código?")
x = 10
if x == 10:
     print(x == 10)
if x > 5:
     print(x > 5)
if x < 10:
     print(x < 10)
else:
     print("else\n")


print("Ejercicio #5\n¿Cuál es la salida del siguiente fragmento de código?")

x = "1"
if x == 1:
    print("uno\n")
elif x == "1":
    if int(x) > 1:
        print("dos\n")
    elif int(x) < 1:
        print("tres\n")
    else:
        print("cuatro")
if int(x) == 1:
    print("cinco\n")
else:
    print("seis\n")

print("Ejercicio #6\n¿Cuál es la salida del siguiente fragmento de código?")

x = 1
y = 1.0
z = "1"

if x == y:
    print("uno")
if y == int(z):
    print("dos")
elif x == y:
    print("tres")
else:
    print("cuatro")
