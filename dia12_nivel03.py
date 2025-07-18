import random

# Ejercicio_1
# Mezcla (revuelve) aleatoriamente los elementos de una lista
def mezclar_lista(lista):
    mezclada = lista[:]
    random.shuffle(mezclada)  # Reorganiza los elementos en orden aleatorio
    return mezclada

# Ejercicio_2
# Genera una lista de 7 números aleatorios únicos del 0 al 9
def numeros_aleatorios_unicos():
    return random.sample(range(10), 7)  # sample evita repetir números
