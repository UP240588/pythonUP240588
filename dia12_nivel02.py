import random

# Ejercicio_1
# Genera una lista de colores en formato hexadecimal (como #a1b2c3)
def lista_colores_hexadecimales(cantidad):
    colores = []
    for _ in range(cantidad):
        color_hex = '#' + ''.join(random.choices('0123456789abcdef', k=6))
        colores.append(color_hex)
    return colores

# Ejercicio_2
# Genera una lista de colores en formato RGB (como rgb(255,0,0))
def lista_colores_rgb(cantidad):
    return [generar_color_rgb() for _ in range(cantidad)]  # Usa la función del ejercicio anterior

# Ejercicio_3
# Genera colores ya sea en formato "hexa" o "rgb" según lo que se indique
def generar_colores(tipo, cantidad):
    if tipo.lower() == 'hexa':
        return lista_colores_hexadecimales(cantidad)
    elif tipo.lower() == 'rgb':
        return lista_colores_rgb(cantidad)
    else:
        return "Tipo de color no soportado"
