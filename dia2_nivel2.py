import math

#Nivel_2

nombre = 'Paola'
apellido = 'Serrano'
pais = 'Mexico'
ciudad = 'Aguascalientes'
edad = '23'
año = '2025'
casado = True
nombre_com = ('Paola, Maricruz, Serrano, Sanchez')
luz_on = False

print(type(nombre))
print(type(apellido))
print(type(pais))
print(type(ciudad))
print(type(edad))
print(type(año))
print(type(casado))
print(type(nombre_com))
print(type(luz_on))

print('Tu nombre contiene estas letras: ',len(nombre))

print('Tu apellido contiene estas letras: ',len(apellido))

num_1 = 5
num_2 = 4
print('variable total: ',num_1+num_2)
print('variable diferencia: ',num_2-num_1)
print('producto: ',num_2*num_1)
print('division: ',num_2/num_1)
print('porcentaje: ',num_2%num_1)
print('exponente: ',num_1**num_2)
print('residuo: ',num_1//num_2)

radio_1 = 30
print('el area del circulo: ',3.1416*radio_1**2)
print('el perimetro del circulo es: ',2*3.1416*radio_1)

cifra = float(input("Ingrese el radio del círculo: "))
print("El area del circulo es: ", 3.141*cifra**2)

nom= input('Ingresa tu nombre: ')
ap= input('Ingresa tu apellido: ')
country= input('Ingresa tu pais: ')
age= input('Ingresa tu edad: ')
