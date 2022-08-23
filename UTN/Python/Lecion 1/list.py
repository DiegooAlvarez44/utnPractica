demo_list = [1, "hola", 1.34, True, [1, 2, 3]]
# Entre corchetes creamos listas para usar


numbers_list = list((1, 2 ,3))
# Adicionando una tupla se puede hacer una
# lista con todos los numeros
print(numbers_list)


r = list(range(1, 100))
# Creamos una lista a partir de este rango
# de 1 hasta 99
print(r)


colors = ["red", "green", "blue"]

print(dir(colors))
# Con dir puedo ver que metodos puedo hacer
# a colors

print(len(colors))
# Con len puedo ver cuantos elementos tengo
# en colors

print(colors[1])
print(colors[2])
print(colors[0])
# Con los corchetes podemos imprimir la 
# posicion 1, 2, 0 de colors

print('green' in colors)
# Buscamos si el elemnto existe en esta lista
# devuelve el valor de true o flase

print(colors)
colors[1] = input("Escriba un color diferente ")
print(colors)
# Con los corchetes declaro que posicion quiero
# cambiar el elemento, le pido al usuario que lo
# cambie 

colors.append("violet")
print(colors)
# Con append solo 
# puedo agregarle un elemento al 
# arreglo

colors.extend(['black', 'pink'])
print(colors)
# Con extend puedo agregar mas de un elemento
# al arreglo

colors.insert(0, "aqua")
print(colors)
# Con insert puedo insertar un elemento en 
# en cualquier lado del arreglo

colors.insert(len(colors), "orange")
print(colors)
# Si conbinamos insert con len (la longitud de colors)
# podemos colocar orange al final de la posicion

colors.pop()
print(colors)
# Con pop podemos quitar elementos

colors.remove('blue')
print(colors)
# Con remove podemos quitar especificamente 

### colors.clear()
# Limpiamos el arreglo
print(colors)

colors.sort()
# Con el metodo sort ordena los elementos 
print(colors, "Metodos ordenados")

colors.sort(reverse=True)
# Con reverse mostramos los elementos ordenados
# al revez
print(colors)

print(colors.index('pink'))
# imprimimos el indice del elemento seleccionado

print(colors.count('violet'))
# Con count contamos cuantas veces esta el elemento
# en la lista