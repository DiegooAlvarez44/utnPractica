# Comenzamos con funciones
# mi_funcion() # No se puede llamar antes de definir a una funcion
# Definimos una funcion
from __future__ import barry_as_FLUFL
from unicodedata import name
from unittest import result


def mi_funcion(): # Para identificar la funcion utilizamos parentesis
    print("Saludos a todos los alumnos de la Tecnicatura")

mi_funcion() # Estamos llamando a la funcion
mi_funcion() # Se puede llamar a una funcion N cantidad de veces

# Desempaquetado de listas o list Unpacking
def show(name, lastname):
    print(name+" "+lastname)
person = ["Diego", "Alvarez"]
show(person[0], person[1]) # Pasamos uno por uno los datos de la lista a la funcion
show(*person)# Esto es lo mismo que lo anterior pero le pasamos todo junto
person2 = ("Diego", "Fernando")
show(*person2)
person3 = {"lastname": "Fregenal", "name":"Diego"}
show(**person3)

numbers = [1, 2, 3, 4, 5] # Aun con el la lista vacia se va a ejercutar el else
for n in numbers:
    print(n)
    if n == 3:
        break # Esta es la unica manera para que no se ejecute el else
else:
    print("Esto se termino")

# List comprehension, lista de comprension
names = ["Diego", "Fernando", "Palacio", "Kuma"]
alongP = [p for p in names if p[0] == 'P'] # Esto es una nueva lista
print(alongP)

bottleC = [{"name":"Quilmes", "country":"Arg"},
{"name":"Corona", "country":"Mx"},
{"name":"Stella Artois", "country":"Belgium"},
]
Arg = [b for b in bottleC if b["country"] == "Arg"]
print(Arg)
print(bottleC)

# Paso de Argumentos (Funciones)
def mi_funcion2(name, lastname):
    print("Saludos a todos")
    print(f"Nombre: {name}, Apellido: {lastname}")
mi_funcion2("Diego", "Fregenal")
mi_funcion2("Fernando", "Alvarez")

# La palabra return en funciones
# Creamos una funcion para sumar
def sumar(a, b):
    return a + b
#resultado = sumar(78, 22)
#print(f"El resultado de la suma es: {resultado}")
print(f'El resultado es: {sumar(45, 44)}')

def sumar2(a:int = 0, b:int = 0): # Le damos un valor por default
    return a + b
resultado = sumar2()
print(f'Reulstado de la suma {resultado}')
print(f'Resultado de la suma: {sumar2(23, 44)}')

# Argumentos, variables en funciones
def listaNombres(*nombres):# Normalmente se utiliza: *args
    for nombre in nombres: # Se va a convertir en una tupla
        print(nombre)

listaNombres('Diego','Lucian','Kuma','Fernando')
listaNombres('Denise', 'Nicole', 'Chudy')

def listaTerminos(**terminos): # Lo mas utilizado es **kwargs para recibir los argumentos
    for llave, valor in terminos.items(): # Para recorrer diccionarios
        print(f'{llave} : {valor}')

listaTerminos() # No recibe nada, nada se va a mostrar
listaTerminos(IDE='Integrated Develoment Enviroment', PK='Primaruy Key')
listaTerminos(nombre='Diego Alvarez')

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 = ['Tito', 'Pedro', 'Carlos']
desplegarNombres(nombres2)
desplegarNombres('Carla')
# desplegarNombres(10, 11) # No es un objetos iterable
desplegarNombres((10, 11)) # La convertimos a una tupla, en un solo elemento no olvidar la coma
desplegarNombres([22, 55]) # La convertimos en una lista

# Funciones Recursivas
def factorial(numero):
    if numero == 1:# Caso Base
        return 1
    else:
        return numero * factorial(numero-1) # Caso Recursivo

usuario = int(input("Digite un numero para calcular su factorial"))
resultado = factorial(usuario)
print(f'El factorial que de {usuario} es : {resultado}')
resultado = factorial(5) # Lo hacemos en codigo duro
print(f'El factorial del numero 6 es: {resultado}')


