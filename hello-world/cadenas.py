fact = "hola. "
fact += "oscar."
#'The Moon has no atmosphere.No sound can be heard on the Moon.'
#print(fact)

#print("-"*40)

fact = "hola ."
fact_2 = fact + "oscar."

#print(fact_2)
#print("-"*40)
# SALTO DE LINEA

salto = "hola \noscar"
#print(salto)
#print("-"*40)
salto2 = '''hola
oscar'''
#print(salto2)

# funcion "title()" comvierte la primrea letra en mayuscula 
ej="hola como estas".title()
print(ej)

ej2 ="hola como estas"
ej2 = ej2.title()
#print(ej2)

print("-"*40)

# para separar cadenas EN LISTAS con **.split** y unirlas con **.join**
texto = "Hola, ¿cómo estás?"
separar = texto.split()     # en ete caso seprada por espacios 
print(separar)
print(separar[-3]) #  esta es la forma de llamar los elementos de la lista
print(separar[1])
print(separar[2])

#RST= ['Hola,', '¿cómo', 'estás?']

unir = "".join(separar) # realizar la union
print(unir)

print()

texto = """Hola, 
¿cómo estás?"""
palabras = texto.split("\n")     # en este caso separada por salto de linea
print(palabras)
# RST= ['Hola, ', '¿cómo estás?']

juntar = '\n'.join(palabras) # se une con el salto de linea \n
print(juntar)
print("-"*40)

# FIND() PARA BUSCAR LA UBICACION DE UNA SUB CADENA 

texto = "Hola, ¿cómo estás?"
posicion = texto.find("cómo")
print(posicion)
# RST= 7
print()

texto = "Hola, ¿cómo estás?"
posicion = texto.find("cómo", 0, 5)
print(posicion)
#RST= -1  ESTE RESULTADO YA QUE NO SE ENCUENTRA EN LA UBICACION ESPECIFICADA

print("-"*40)

# para extraer datos numericos de cadenas de texto con bucles
edad = " mi edad es de 41 años de  "
for i in edad.split():
    if i.isnumeric():
        print(i)
        i = int(i)
        print(i + 4)  # no olvidar que esta operacion va dentro del bucle
print()

# la operacion fuera de bucle
edad = " mi edad es de 41 años de  "
num = None

for i in edad.split():
    if i.isnumeric():
        num = i

if num:
    a = int(num) + 3
    print(a)

print("-"*40)
# comprueba si la cadena INICIA con lo indicado
texto = "Hola, ¿como estás?"
if texto.startswith("Hola"):
    print("La cadena comienza con 'Hola'")
else:
    print("La cadena no comienza con 'Hola'")

com = texto.startswith("H")
print(com)

print("-"*40)
# compueba si FINALIZA con lo escogido
texto = "Hola, ¿como estás?"
ver = texto.endswith("s")
print(ver)

print("-"*40)

# remplazar caracteres
tex = "Hola Raul".lower()
rem = tex.replace("raul", "oscar")
print(rem)
