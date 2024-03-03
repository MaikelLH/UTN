
# If
'''Como puedes ver, tender la cama, tomar una ducha y dormir y 
soñar se ejecutan condicionalmente, cuando sheep_counter alcanza el límite deseado.

Alimentar a los perros, sin embargo, siempre se hace (es decir, 
la función feed_the_sheepdogs() no tiene sangría y no pertenece al bloque if, 
lo que significa que siempre se ejecuta).'''

if sheep_counter >= 120:
    make_a_bed()
    take_a_shower()
    sleep_and_dream()
feed_the_sheepdogs()

# If-Else
'''Si la condición se evalúa como True (su valor no es igual a cero), 
la instrucción perform_if_condition_true se ejecuta, y la sentencia 
condicional llega a su fin.
Si la condición se evalúa como False (es igual a cero), 
la instrucción perform_if_condition_false se ejecuta, 
y la sentencia condicional llega a su fin.'''

if true_or_false_condition:
    perform_if_condition_true
else:
    perform_if_condition_false

'''Si el clima es bueno, saldremos a caminar. De lo contrario, 
iremos al cine. No importa si el clima es bueno o malo, almorzaremos 
después (después de la caminata o después de ir al cine).'''

#Ejemplo 1

if the_weather_is_good:
    go_for_a_walk()
else:
    go_to_a_theater()
have_lunch()

# Ejemplo 2

if the_weather_is_good:
    go_for_a_walk()
    have_fun()
else:
    go_to_a_theater()
    enjoy_the_movie()
have_lunch()

# Sentencias if-else anidadas
'''Lee lo que hemos planeado para este Domingo. 
Si hay buen clima, saldremos a caminar. 
Si encontramos un buen restaurante, almorzaremos allí. 
De lo contrario, vamos a comer un sandwich. 
Si hay mal clima, iremos al cine. 
Si no hay boletos, iremos de compras al centro comercial más cercano.'''

if the_weather_is_good:
    if nice_restaurant_is_found:
        have_lunch()
    else:
        eat_a_sandwich()
else:
    if tickets_are_available:
        go_to_the_theater()
    else:
        go_shopping()

'''Este uso de la sentencia if se conoce como anidamiento; 
recuerda que cada else se refiere al if que se encuentra en 
el mismo nivel de sangría; se necesita saber esto para determinar 
cómo se relacionan los if y los else .
Considera como la sangría mejora la legibilidad y hace que el 
código sea más fácil de entender y rastrear.'''

# elif

'''elif se usa para verificar más de una condición, y para 
detener cuando se encuentra la primera sentencia verdadera.'''

'''Nuestro siguiente ejemplo se parece a la anidación, 
pero las similitudes son muy leves. Nuevamente, cambiaremos 
nuestros planes y los expresaremos de la siguiente manera: 
si hay buen clima, saldremos a caminar, de lo contrario, 
si obtenemos entradas, iremos al cine, de lo contrario, 
si hay mesas libres en el restaurante, vamos a almorzar; 
si todo falla, regresaremos a casa y jugaremos ajedrez.'''

if the_weather_is_good:
    go_for_a_walk()
elif tickets_are_available:
    go_to_the_theater()
elif table_is_available:
    go_for_lunch()
else:
    play_chess_at_home()

'''La forma de ensamblar las siguientes sentencias if-elif-else 
a veces se denomina cascada.

Se debe prestar atención adicional a este caso:

No debes usar else sin un if precedente.
else siempre es la última rama de la cascada, independientemente de si has usado elif o no.
else es una parte opcional de la cascada, y puede omitirse.
Si hay una rama else en la cascada, solo se ejecuta una de todas las ramas.
Si no hay una rama else, es posible que no se ejecute ninguna de las opciones disponibles.
'''

