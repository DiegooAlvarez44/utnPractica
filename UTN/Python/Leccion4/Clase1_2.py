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
nombres.append('Marcelo')
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

