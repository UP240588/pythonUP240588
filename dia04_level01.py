#Nivel 1 

#1
p1 = "Treinta"  
p2 = "días"
p3 = "de"
p4 = "Python"
space = ' '
print(p1+space+p2+space+p3+space+p4)

#2
pa1 = "Codificación"
pa2 = "para"
pa3 = "todos"
esp = " "
print(pa1+esp+pa2+esp+pa3)

#3
empresa = 'Codificación para todos' 

#4, 5, 6, 7, 8
print(empresa)
print(len(empresa))
print(empresa.upper())
print(empresa.lower())
print(empresa.capitalize())
print(empresa.title())
print(empresa.swapcase())

#9
primer_pal = empresa[:empresa.find(" ")] 
print("Primer palabra: ",primer_pal)

#10
if empresa.find("Codificación") != -1:
    print("'Codificación' fue encontrada usando find()")
else:
    print("'Codificación' no fue encontrado usando find()")

try:
    posicion = empresa.index("Codificación")
    print("'Codificación' fue encontrada usando index() en la posición {posicion}")
except ValueError:
    print("'Codificación' no fue encontrado usando index()")

if "Codificación" in empresa:
    print("'Codificacion' fue encontrado usando 'in'")
else: 
    print("'Codificación' no fue encontrado usando 'in'")

#11
new_tex = empresa.replace("Codificación", "Python")
print(new_tex)

#12
nuevo = new_tex.replace("todos", "todas")
print(nuevo)

#13
palabras = empresa.split(" ")
print(palabras)

#14
text = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
compa = text.split(", ")
print(compa)

#15
caracter = empresa[0]
print("El cáracter 0 en la oración es: ", caracter)

#16
ult_ind = len(empresa)
print("El último índice de la cadena es: ", ult_ind)

#17
caract = empresa[10]
print("El cáracter 10 en la oración es: ", caract)

#18
frase = "Paython para todos"
palabrass = frase.split()
acronimo = "".join([palabra[0].upper() for palabra in palabrass])
print("El acrónimo es: ", acronimo)

#19
palabras2 = empresa.split()
acronimo_2 = "".join([palabra[0].upper() for palabra in palabras2])
print("El acrónimo es: ", acronimo_2)

#20
position = empresa.index('C')
print("La primera aparición de la 'C' en la oración:", position)

#21
letraF = empresa.index('f')
print("La primera aparición de la 'F' en la oración:", letraF)

#22
letrao = empresa.rfind('o')
print("La última aparación de la 'O' en la oración:", letrao)

#23
oracion= "No puedes terminar una oración con 'because' porque 'because' es una conjugación"
encontrar = oracion.index('because')
print("La primer posición donde aparece 'because' en la oración:", encontrar)

#24
encontrar_ult = oracion.rfind('because')
print("La última aparición de la palabra 'because' en la oración:", encontrar_ult)

#25
frasee = "No puedes terminar una oración con because because because es una conjugación"
inicio = frasee.find('because')
fin = inicio +  len("because because because")
frasefinal = frasee[inicio:fin]
print("Frase extraída:", frasefinal)

#26
possicion = frasee.find("because")
print(possicion)

#27
inicio = frasee.find("because because because")
longitud = len("because because because")
frase_cortada = frase[inicio:inicio + longitud]
print(frase_cortada)

#28
resultad0 = empresa.startswith("Codificación")
print(resultad0)

#29
resultad = empresa.endswith("coding")
print(resultad)

#30
texto = 'Codificación para todos'
texto_limpio = texto.strip()
print(f"Antes: '{texto}'")
print(f"Después: '{texto_limpio}'")

#31
print("30DaysOfPython".isidentifier())        
print("thirty_days_of_python".isidentifier()) 

#32
librerias = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
resultado1 = '# '.join(librerias)
print(resultado1)

#33
frases = "Estoy disfrutando de este desafío._ Solo me pregunto qué sigue."
print(frases)

#34
texto = "Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
print(texto)

#35
radio = 10
area = 3.14 * radio ** 2
mensaje = "El área del círculo con radio {} en {} metros cuadrados.".format(radio, area)
print(mensaje)

#36
a = 8
b = 6

print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))  
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} * {} = {}".format(a, b, a * b))