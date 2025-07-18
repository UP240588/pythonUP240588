
#Level_2

#1
edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
edades.sort()

edad_minima = edades[0]
edad_maxima = edades[-1]

edades.append(edad_minima)
edades.append(edad_maxima)

edades.sort()

n = len(edades)
if n % 2 == 1:
    mediana = edades[n // 2]
else:
    mediana = (edades[n//2 - 1] + edades[n//2]) / 2

promedio = sum(edades) / n

rango = edad_maxima - edad_minima

abs_min = abs(edad_minima - promedio)
abs_max = abs(edad_maxima - promedio)

print("Lista ordenada con min y max agregados:")
print(edades)
print(f"Edad mínima: {edad_minima}")
print(f"Edad máxima: {edad_maxima}")
print(f"Mediana: {mediana}")
print(f"Promedio: {promedio:.2f}")
print(f"Rango: {rango}")
print(f"Valor absoluto de (min - promedio): {abs_min:.2f}")
print(f"Valor absoluto de (max - promedio): {abs_max:.2f}")


#1
countries = ['China', 'India', 'USA', 'Indonesia', 'Pakistan', 'Brazil', 'Nigeria']
n = len(countries)

if n % 2 == 1:
    indice_medio = n // 2
    paises_medio = countries[indice_medio:indice_medio+1]
else:
    indice_medio1 = n // 2 - 1
    indice_medio2 = n // 2
    paises_medio = countries[indice_medio1:indice_medio2+1]
print("País(es) del medio:")
print(paises_medio)


#2
countries = ['China', 'India', 'USA', 'Indonesia', 'Pakistan', 'Brazil', 'Nigeria']
n = len(countries)

if n % 2 == 0:
    mitad = n // 2
else:
    mitad = n // 2 + 1
primera_mitad = countries[:mitad]
segunda_mitad = countries[mitad:]
print("Primera mitad:")
print(primera_mitad)
print("Segunda mitad:")
print(segunda_mitad)


#3
ciudades = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

primera_ciudad, segunda_ciudad, tercera_ciudad, *escandinavos_ciudades = ciudades

print("Primer país:", primera_ciudad)
print("Segundo país:", segunda_ciudad)
print("Tercer país:", tercera_ciudad)
print("Países escandinavos:", escandinavos_ciudades)