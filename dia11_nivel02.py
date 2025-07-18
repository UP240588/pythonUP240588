# Ejercicio_1

def pares_e_impares(n):
    pares = sum(1 for i in range(n + 1) if i % 2 == 0)
    impares = n + 1 - pares
    return f"La cantidad de impares es {impares}. La cantidad de pares es {pares}."

# Ejercicio_1 (repetido en el original)

import math
def factorial(n):
    return math.factorial(n)

# Ejercicio_2

def esta_vacio(param):
    return not bool(param)  # Devuelve True si está vacío, False si no

# Ejercicio_3
from statistics import mean, median, variance, stdev
from collections import Counter


def calcular_media(lista):
    return mean(lista)


def calcular_mediana(lista):
    return median(lista)


def calcular_moda(lista):
    return Counter(lista).most_common(1)[0][0]


def calcular_rango(lista):
    return max(lista) - min(lista)


def calcular_varianza(lista):
    return variance(lista)

# Calcula la desviación estándar (raíz cuadrada de la varianza)
def calcular_desviacion_estandar(lista):
    return stdev(lista)
