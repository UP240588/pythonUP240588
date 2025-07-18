import random
import string

# Ejercicio_1
# Genera un ID de usuario aleatorio de 6 caracteres (letras y números)
def id_usuario_aleatorio():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

# Ejercicio_2
# Genera múltiples IDs personalizados según lo que el usuario indique
def generar_ids_por_usuario():
    longitud = int(input("Ingresa el número de caracteres por ID: "))
    cantidad = int(input("Ingresa cuántos IDs quieres generar: "))
    for _ in range(cantidad):
        print(''.join(random.choices(string.ascii_letters + string.digits, k=longitud)))

# Ejercicio_3
# Genera un color aleatorio en formato RGB
def generar_color_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"
