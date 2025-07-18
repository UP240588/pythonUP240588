#dia 3

edad = 23
altura = 1.70
num = complex(input("Ingrese un número complejo: "))

base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese el altura del triángulo: "))
area = 0.5*base*altura
print("El area del triángulo es: ", area)

a = float(input("Ingrese lado a: "))
b = float(input("Ingrese lado b: "))
c = float(input("Ingrese lado c: "))
perim = a+b+c
print("El perímetro del triángulo es: ", perim)

#6
largo = float(input("Ingrese el altura del rectángulo: "))
ancho = float(input("Ingrese la base del rectángulo: "))
area_rec = largo*ancho
print("El área del rectángulo es: ",area_rec)
perimetro = 2*(ancho + largo)
print("El perímetro del rectángulo es: ",perimetro)

#7
rad = float(input("Ingrese el radio del círculo: "))
pi = 3.14
area_cir = pi*rad*rad
circum = 2*pi*rad
print("El área del círculo es: ",area_cir)
print("La circunferencia del círculo es: ",circum)

#8
m = 2
b = -2
x_intercept = -b / m
print("Pendiente:", m)
print("Intersección en Y:", b)
print("Intersección en X:", x_intercept)

#9
import math
x1, y1 = 2, 2
x2, y2 = 6, 10
pend = (y2 - y1) / (x2 - x1)
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Pendiente:", pend)
print("Distancia euclidiana:", distance)

#valor de Y
x1= -4
y1= x1**2 + 6*x1 + 9
print("Si x= ", x1, "entonces y= ", y1)
x2= -3
y2= x2**2 + 6*x2 + 9
print("Si x= ", x2, "entonces y=", y2)
x3= -2
y3= x3**2 + 6*x3 + 9
print("Si x= ", x3, "entonces y=", y3)
x4= -1
y4= x4**2 + 6*x4 + 9
print("Si x= ", x4, "entonces y=", y4)

#verificar cuando Y es igual a 0
if y1 == 0:
    print("y es 0 cuando x =", x1)
if y2 == 0:
    print("y es 0 cuando x =", x2)    
if y3 == 0:
    print("y es 0 cuando x =", x3)
if y4 == 0:
    print("y es 0 cuando x =", x4)

#longitud PYTHON y DRAGON
p1 = len("python")
p2 = len("dragon")
print("Longitud de 'python': ", len('python'))
print("Longitud de 'dragon': ", len('dragon'))

comparacion = p1 > p2
print("¿La longitud de 'python' es mayor que la de 'dragon'? ", comparacion)

#comprobar si ON está en las palabras
palabra= "python"
palabra= "dragon"

resul = ("on" in palabra) and ("on" in palabra)
print("¿La cadena 'on' está en ambas palabras 'python' y 'dragon'? ", resul)

#comprobar que jerga no se encuentra en la oracion
oracion= input("Ingrese una oración: ")
com = ("jerga" in oracion)
print("En la oración ¿se encuentra la palabra jerga? ", com)

#cambiar tipo de variable a PYTHON 
texto = "Python"
longitud = len(texto)
print("Longitud (entero): ", longitud)
flo = float(longitud)
print("Longitud como número flotante: ", flo)
cad = str(flo)
print("Longitud como cadena: ", cad)

#numero par o impar
num = int (input("Ingrese un número: "))
if (num %2 == 0): 
    print("El número es par")
else:
    print("El número es impar")

#comprobar si el residuo de 7 entre 3 es igual a 2.7
div = 7 % 3
r = 2.7
compar = div == r
print("¿El residuo es igual a 2.7? ", compar)

#comprobar si '10' es igual a 10
j = '10'
l = 10
ad = type(j) == type(l)
print("¿El tipo de '10' es igual al tipo de 10? ", ad)

#comprobar si '9.8'es igual a 10
f = int(9.8)
c = 10
run = type(f) == type(c)
print("¿El tipo de 9.8 es igual al tipo de 10? ", run)

#salario
hrs= float(input("Ingrese las horas: "))
tari= float(input("ingrese la tarifa por hora: "))
print("Su salario es de: ", hrs*tari)

#cuantos segundos vive una persona
year = int(input("Ingrese los años que ha vivido: "))
print("Los segundos que ha vivido son: ", year*31536000)

#imprimir tabla
print(1, 1, 1, 1, 1)
print(2, 1, 2, 4, 8)
print(3, 1, 3, 9, 27)
print(4, 1, 4, 16, 64)
print(5, 1, 5, 25, 125)