import math

# Ejercicio_1
# Verifica si un número es primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):  # Solo revisa hasta la raíz cuadrada de n
        if n % i == 0:
            return False
    return True

# Ejercicio_2
# Verifica si todos los elementos de una lista son únicos (sin repetir)
def elementos_son_unicos(lista):
    return len(lista) == len(set(lista))  # Convierte a conjunto, que elimina duplicados

# Ejercicio_3
# Verifica si todos los elementos de una lista son del mismo tipo (todos enteros, o todos cadenas, etc.)
def son_del_mismo_tipo(lista):
    return all(type(x) == type(lista[0]) for x in lista)

# Ejercicio_4
# Verifica si un nombre es válido como nombre de variable en Python
def es_variable_valida(nombre):
    return nombre.isidentifier()  # Ej: "mi_variable" sí es válido, "123abc" no lo es
