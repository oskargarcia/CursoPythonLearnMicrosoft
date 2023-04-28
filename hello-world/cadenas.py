fact = "hola. "
fact += "oscar."
#'The Moon has no atmosphere.No sound can be heard on the Moon.'
print(fact)

print("-"*40)

fact = "hola ."
fact_2 = fact + "oscar."

print(fact_2)
print("-"*40)
# SALTO DE LINEA

salto = "hola \noscar"
print(salto)
print("-"*40)
salto2 = '''hola
oscar'''
print(salto2)

# funcion "title()" comvierte la primrea letra en mayuscula 
ej="hola como estas".title()
print(ej)

ej2 ="hola como estas"
ej2 = ej2.title()
print(ej2)

print("-"*40)

# para separar cadenas EN LISTAS
texto = "Hola, ¿cómo estás?"
palabras = texto.split()     # en ete caso seprada por espacios 
print(palabras)
print(palabras[-3]) #  esta es la forma de llamar los elementos de la lista
print(palabras[1])
print(palabras[2])


#RST= ['Hola,', '¿cómo', 'estás?']
print()

texto = """Hola, 
¿cómo estás?"""
palabras = texto.split("\n")     # en este caso separada por salto de linea
print(palabras)
# RST= ['Hola, ', '¿cómo estás?']

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

