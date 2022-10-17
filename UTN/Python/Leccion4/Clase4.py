"""
#Ejercicio 1: Eliminar duplicados de una lista
# Escriba un programa donde tenga una lista
#y que a continuacion elimine los elementos repetidos,
# por ultimo mostrar la lista

#Creamos una lista

import math


lista = [1, 2, 3, "Diego", 4, 5, 6, "Fernando"]
# conjunto de ser(lista) # Convertimos la lista a un conjuto de tipo set
# lista = list(conjunto) # Convertimos el conjunto a una lista
lista = list(set(lista)) # La conversion hecha en una sola linea de codigo
print(lista)



list = [1,2,3,45,3,3,4,5]
cleanList = []
for i in list: 
    if i not in cleanList: cleanList.append(i)
    print(f"Lista original: {list}\n" f"Lista sin elementos repetidos: {cleanList}")

#Ejercicio 2: Operaciones de conjuntos con listas 
#Escribe un programa que tenga 2 listas y que a continuacion
#Cree las siguientes listas (en las que no deben haber repeticiones)
# 1 Lista de palabras que aparecen en las listas
# 2 Lista de palabras que aparecen en la primera lista, pero que no en la segunda
# 3 Lista de palabras que aparecen en la segunda lista, pero no en la primera
# 4 lista de palabras que aparecen en ambas listas

lista1 = [1,2,3,4,5,6,4,3,2,1,2,5]
lista2 = [6,3,4,6,1,2,3,5,8,2,3,5]

# Elmimnar los elemtnso repetidos  de ambas listas

conjunto1 = set(lista1)
conjunto2 = set(lista2)

union = conjunto1 | conjunto2 # Unimos los dos conjuntos
solo1 = conjunto1 - conjunto2 # Solo muestra el conjunto1
solo2 = conjunto2 - conjunto1 # Solo se muuestra el primerop 
interseccion = conjunto1 & conjunto2 # Mostramos ambas listas

print(f"Lista de palabras que aparecen en las listas: {union}")
print(f"Lista de palabras que aparecen en la primera lista, pero no en la segunda: {solo1}")
print(f"Lista de palabras que aparecen en la segunda lista, pero no en la primera: {solo2}")
print(f"Lista de palabras que aparecen en ambas listas: {interseccion}")

# Agregar personajes a una lista 
# Escriba un programa donde cree una lista con los siguientes personajes del señor de los anillos
# Dentro de una lista vacia hayq que llenarla con diccionarios y c ada diccionario va a contener un personaje
# Nombre: Aragon
# Clase: Guerrero
# Raza: Dunaban del Norte

personajes = []
# Creamos diccionarios
P = {'Nombre': 'Aragon', 'Clase': 'Guerrero', 'Raza':'Dunadan del Norte'}
personajes.append(P) # Agregamos a la lista un personaje
P = {'Nombre':'Legolas', 'Clase': 'Arquero', 'Raza': 'Sindar'}
personajes.append(P)
P = {'Nombre':'Gandalf', 'Clase': 'Arquero', 'Raza': 'Elfo Sindar'}
personajes.append(P)
print(personajes)

P = input("Escribir ")
personajes.append(P)




# Ejercicio de Matematica
# Para sacar la raiz cuadrada de un numero positivo
numero = int(input("Digite un numero positivo "))
while numero < 0:
    print('Error -> Deberia ser un numero positivo')
    numero = int(input('Digite un numero positivo: '))
print(f'\nSu raiz cuadrad es: {math.sqrt(numero):.2f}')

# Ejercicio 4.6
# Ejercicio 1 llenar una lista
# Llenar una lista con los numeros de 1 al 50, luego mostra
# la lista con el bucle for, los elementos deben mostrarse de la 
# siguiente forma:
# 1-2-3-4-...-50
lista = range(1, 51)
for i in lista:
    print(i, end='-')
lista
# Otra forma
lista4 = []
i = 1
while i <= 50:
    lista4.append(i)
    i += 1
for i in lista4:
    print(i, end='-')
"""
"""
# Ejercico 4.7 
# Ejercicio 2: Modificar los elementos de una lista
# Llenar una lista con los numeros del 1 al 10,
# Luego de modificar los elementos de la lista 
# multiplicandolos por un valor ingresado por el usuario

lista3 = range(1, 11)
print("Lista sin modificar ")
for i in lista3:
    print(i, end="-")
numUsuario = int(input("Numero para multiplicar los elementos de la lista: "))
for i in lista3:
    resultado = numUsuario * i
    print(resultado, end=("-"))
"""
# 4.8 Ejercicio 3: Insertar elementos ordenados funcion sort()

# Pedir Numero y meterlos en una lista, cuando el
# usuario introduzca un numero 0, nuestro programa
# dejaria de insertar.
# Por ultimo, mostrar los numeros ordenados de menor a mayor
numeros_enLista = []
numero = 0
i=False
while not i:
    numero = int(input("Digite un numero, digite 0 para terminar: "))
    if numero == 0:
        i=True
    else:
        numeros_enLista.append(numero)

numeros_enLista.sort()
print(numeros_enLista)
