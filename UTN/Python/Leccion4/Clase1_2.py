#Lista = Diego, Lucian, Fernando, Braian 


nombres = ["Diego", "Lucian", "Fernando","Braian"]
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[3])
print(nombres[-1]) # -1 muestra el ultimo de la lista
print(nombres[-2]) # -2 muestra el anteultimo de la lista
print(nombres[0:2]) # muestra del indice 0, 1, lo que hay despues del 2 no lo muestra
print(nombres[ :3]) #  Empieza desde el indice y Omite la posicion 3
print(nombres[1: ]) #  Empieza desde el indice 1 y sigue hacia el final de la lista
# Modificar un valor de la lista
nombres[2] = "Daniel"
print(nombres)
# Iterar una lista 
for nombre in nombres: # nombre es sigular, la lista es plural
    print(nombre)
else:
    print("Se acabaron los elementos de la lista")
# Preguntamos cuantos elementos tiene 
print(len(nombres)) #le pasamos como parametro a la lista
# Agregamos un elemento 
nombres.append('Marcelo') # Elemento string
nombres.append(3) # Elemento entero
nombres.append(True) # Elemento booleano
nombres.append(10.45) # Elemento Float
nombres.append([4, 5]) # Una lista
nombres.append(7)
print(nombres)
# Insertar un elemento en un indice especifico de la lista
nombres.insert(1, 'Alberto')
print(nombres)
nombres.insert(3, 'Cristobal')
print(nombres)
# Eliminamos un elemento de la lista
nombres.remove('Diego')
print(nombres)
# Eliminar el ultimo elemento de la lista 
nombres.pop()
print(nombre)
# Eliminar un elementos especifico 
del nombres[2] # del significa delete (eliminar)
print (nombres)
# Eliminar, borrar o limpiar todos los elementos 
nombres.clear()
print(nombres)
# Eliminar la LISTA 
#del nombres# Elimina la lista
print(nombres, "Eliminamos la lista")

# EJecicio 1

nombres = [0,1,2,3,4,5,6,7,8,9]
for nombre in nombres:# nombre es  singular, la lista es plural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')

for nombre in nombres:
    if (nombre % 3 == 0):
        print(nombre)
    
# ejecico 1 

print('Rango de 0 a 10 con numeros divisibles entre 3')
for i in range(11):
    if i % 3 == 0:
        print(i)

# Ejercicio 2
print('Ejercicio 2 rango con valores de inicio = 2 y fin = 6')
rango = range(2, 7)
for i in rango:
    print (i)

# Ejercicio 3
print('Ejercicio 3 rango de 3 a 10 con incremento de 2 en 2')
rango = range(3, 10, 2)
for i in rango:
    print(i)


"""
# Defnimos una tupla 
cocina = ("chuchara", "cuchillo", "tenedor")
print(len(cocina))

# Acceder a un elemento de la tupla para eso utilizamos corchetes en ves de parentesis  
print(cocina[0])
# Mostrar de manera invera
print(cocina[-1])
# Acceder a un rango 
print(cocina[0:2])

# Ejemplo 
verduras = ('papa',) # Una tupla necesita aunque sea de un elemento: la coma ,

# Recorremos los elementos de la tupla con un ciclo for
for cocinar in cocina: #Print esta usasndo \n para saltos de lineas
    print(cocinar, end=' ') # Usamos end=' ' para que elimine los saltos de lineas

cocinaLista = list(cocina)
cocinaLista[0] = 'Plato'
cocina = tuple(cocinaLista)
print('\n', cocina)

#Ejercicio tupla 
tubla = (13, 1, 8, 3, 2, 5, 8)

num = []
for i in tubla:
    if i < 5:
        num.append(i)
print(num)
"""
"""
# SET
planetas = {'Marte', 'Jupiter', 'Venus'}
print(len(planetas)) # Usamos la funcion len = length significa largo

# Revisar si un elemento exciste dentro del set
print('Marte' in planetas) # Nos devuelve un booleano

#agregamos un elemento 
planetas.add('Tierra')
print(planetas)

#Eliminar un elemento, puede arrojar un error si el elemento no existe 
planetas.remove('Jupiter')
print(planetas)

#Eliminar set o conjunto 
del planetas
#print(planetas)# Nos ira el error NameError: name 'planetas' is not defined por que con DEL lo elminamos

# DICCIONARIOS
#'Messi':10 Un diccionario esta compuesto por dos elementos 
# UNA LLAVE Y UN VALOR 
####  dict(key,value)
diccionario = {
    'IDE':'Integrated development Environment',
    'POO':'Programacio Orientada a Objetos',
    'SABD':'Sistema de Administracion de Base de Datos'
}
#Verificar la cantidad de elementos ene el diccionario 
print(len(diccionario))
print(diccionario)

# Acceder a un diccionario con la llave(key)
print(diccionario['IDE'])

#Otra forma de recuperar un elemento 
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

#Modificamos un elemento 
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

# Como reccorer los Diccionarios 
for termino in diccionario: # Recorremos solo buscando las llaves
    print(termino)
"""
"""
# Neceistamos una funcion para recorrer un diccionario 
for termino, valor in diccionario.items(): #Funcion .items()
    print(termino, valor)

# Otras maneras de acceder a un diccionario 
for termino in diccionario.keys():
    print(termino) # Solo muestra las llaves

for valor in diccionario.values(): # Usamos funcion para acceder al valor
    print(valor) # Solo muestra valor; value

# Comprobar la existencia de algun elemento 
print('IDE' in diccionario) # devuelve un booleano

# Agregar un elemento
diccionario['PK'] = 'Primary key'
print(diccionario)

# Eliminamos un elemento 
diccionario.pop('POO') # tenemos que escribir la llave 
print(diccionario)

# Para Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar un Diccionario 
del diccionario # El diccionario se borro
#print(diccionario) #Error

# Concatenacion LISTAS
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6, 1]
lista3 = lista1+lista2
print(lista3)

lista3.extend([7, 8, 9, 1]) # Funcion para agregar varuis elementos a una lista
print(lista3)

print(lista3.index(5)) # Funcion para ubicar en que indice esta el valor ingresado 
# print(lista3.index(0)) # esto daria un error por nos ser el elemento parte de la lista

# Como saber cuantos valores repetidos hay dentro de una lista
print(lista3.index(1)) # cuenta cuantos valores iguales hay dentro de la lista

# Para poner al reves una lista
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos
lista3 = lista3 * 2
print(lista3)

# Metodos de ordenamiento, en python es una funcion
lista3.sort() # Ordena los elementos ascendentemente
print(lista3)
lista3.sort(reverse=True) # Ordena descendentemente
print(lista3)

# Repaso de Tuplas 
tupla = (4, 'Hola', 8.78, [1, 2, 78], 4, 'Hola') # Puede tener diferentes tipos de datos dentro
print(tupla)

print(4 in tuple) # Accion booleana, su respuesta es de tipo booleana
# Lo que podemos usar dentro de tuplas son: index, count, len
# En tuplas se puede convertir de tupla a lista y de lista a tupla

# Repaso de set o conjunto
# para definir un conjunto
conjunto2 = set()
conjunto1 = {'bye', }
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)
conjunto1.add('hola')
print(conjunto1)
print(3 not in conjunto1) # Preguntamos si el numero 3 NO esta en el conjunto1

# Como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto2) # Nos devuelve como respuesta un booleano

# Operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2 # La linea una los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 # Que elementos tienen en comun
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 # Asigna el valor que esta en el conjunto1 y no en el conjunto2
print(conjunto3)
conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 # elementos que no comparten o que diferentes entre ambos
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3)) # Aqui preguntamos si un conjunto es un subconjunto dentro de otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1)) # Preguntamos si los elementos del conjunto1 estan dentro del 3
print(conjunto3.issuperset(conjunto2)) # Si es verdadero quiere decir que el conjunto3 es un superconjunto 
print(conjunto2.issuperset(conjunto3))

# Como saber si ambos conjuntos son disconexos, esto es si no comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2)) # No hay cosas en comun

# Convertir un conjunto totalmente en inmutable
conjunto1 = frozenset # Esto hace que el conjunto sea totalmente inmutable
# No se puede agregar, modificar ni eliminar elementos del conjunto

# Repaso Diccionarios
diccionarioNuevo = {'Azul':'Blue', 'Rojo': 'Red', 'Green':'Verde', 'Amarillo':'Yellow'}
print(diccionarioNuevo)

# Como eliminar
del (diccionarioNuevo['Azul'])
print(diccionarioNuevo)

# Los diccionarios pueden almacenar diferente tipos de datos
diccionario2 = {'Ariel':{'Edad':40, 'Altura':1.83}, 'Osvaldo':[45, 1.85], 'Natalia':[35, 1.87]}
print(diccionario2)

seleccionArgentina = {
    10: {'Nombre':'Lionel Messi', 'Edad':35, 'Altura': 1.70, 'Precio':"50 Millones", 'Posicion': 'Extremo Derecho'},
    20: {'Nombre':'Giovali Lo Celso', 'Edad':26, 'Altura':1.77, 'Precio':'22 MiIllones', 'Posicion':'Mediocentro'},
    17: {'Nombre':'Cristian Romero', 'Edad':24  , 'Altura':1.85, 'Precio':'48 Millones', 'Posicion':'Defensa Central'},
    11: {'Nombre':'Angel Di Maria', 'Edad':34, 'Altura': 1.80, 'Precio': '12 Millones', 'Posicion':'Extremo Derecho'},
    19: {'Nombre':'Nicolas Otamendi', 'Edad':34, 'Altura':1.83, 'Precio': '3.5 Millones', 'Posicion':'Defensa Central'}
}

for llave, valor in seleccionArgentina.items():
    print(llave, valor)

# Como tarea agregar por lo menos 4 jugadores mas al diccionario: seleccionArgentina
print('Tenemos cargados en el diccionario la cantidad de: ', end=' ')
print(len(seleccionArgentina))

# Pilas usando listas
pila = [1, 2, 3]

# Agregar elementos a la pila por el final 
pila.append(4)
pila.append(5)
print(pila)

# Sacamos elementos desde el final
elementoBorrado = pila.pop() # Quita el ultimo elemento y lo guarda en la variable
print(f'Sacamos el elemento: {elementoBorrado}')
print(f'La pila ahora quedo asi: {pila}')

# Colas con listas
# Estructura de datos de tipo fifo(first input / first output)
cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']

# Agregamos elementos al final de la cola
cola.append('Natalia')
cola.append('Jose')
print(cola)

# Sacamos elementos de la cola
seRetira = colapop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = colapop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = colapop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = colapop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = colapop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)
"""
