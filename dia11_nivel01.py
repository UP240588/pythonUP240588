# Ejercicio_1
def sumar_dos_numeros(a, b):
    return a + b

# Ejercicio_2
import math
def area_del_circulo(r):
    return math.pi * r * r  # π * radio²

# Ejercicio_3
def sumar_todos_los_numeros(*args):
    if all(isinstance(x, (int, float)) for x in args):  # Verifica si todos son números
        return sum(args)
    return "Todos los argumentos deben ser números"

# Ejercicio_4
def convertir_celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

# Ejercicio_5
def verificar_estacion(mes):
    mes = mes.lower()  # Convierte el mes a minúsculas
    if mes in ['september', 'october', 'november']:
        return 'Otoño'
    elif mes in ['december', 'january', 'february']:
        return 'Invierno'
    elif mes in ['march', 'april', 'may']:
        return 'Primavera'
    elif mes in ['june', 'july', 'august']:
        return 'Verano'
    else:
        return 'Mes inválido'

# Ejercicio_6
def calcular_pendiente(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

# Ejercicio_7
def resolver_ecuacion_cuadratica(a, b, c):
    d = b ** 2 - 4 * a * c  # Discriminante
    if d < 0:
        return "No tiene raíces reales"
    elif d == 0:
        raiz = -b / (2 * a)
        return (raiz,)
    else:
        raiz1 = (-b + math.sqrt(d)) / (2 * a)
        raiz2 = (-b - math.sqrt(d)) / (2 * a)
        return (raiz1, raiz2)

# Ejercicio_8
def imprimir_lista(lst):
    for elemento in lst:
        print(elemento)

# Ejercicio_9
def invertir_lista(lst):
    return lst[::-1]  # Devuelve la lista al revés

# Ejercicio_10
def capitalizar_elementos_lista(lst):
    return [elemento.capitalize() for elemento in lst]

# Ejercicio_11
def agregar_elemento(lst, item):
    lst.append(item)
    return lst

# Ejercicio_12
def eliminar_elemento(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

# Ejercicio_13
def suma_de_numeros(n):
    return sum(range(n + 1))  # Suma del 0 hasta n

# Ejercicio_14
def suma_de_impares(n):
    return sum(i for i in range(n + 1) if i % 2 != 0)

# Ejercicio_15
def suma_de_pares(n):
    return sum(i for i in range(n + 1) if i % 2 == 0)
