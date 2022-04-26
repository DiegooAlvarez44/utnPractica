myStr = "Hola Mundo Soy Diego"

# Mostramos las propiedes o metodos que podemos hacer 
# con el tipo de dato string



print(dir(myStr))
print(" ")
# El metodo dir es para mostrar todos los metodos

print(myStr.upper())
print(" ")
# Cambiamos con el metodo upper la variable myStr
# todo a mayuscula

print(myStr.lower())
print(" ")
# Cambiamos con el metodo lower la variable myStr 
# todo a minuscula

print(myStr.swapcase())
print(" ")
# Invierte lo que antes estaba en mayuscula a minuscula
# y sucesivamente, el metodo swapcase

print(myStr.capitalize())
print(" ")
# Este metodo mantiene solo la primera letra de la
# la primera palabra en mayuscula 


print(myStr.replace('Hola', "Adios"))
print(" ")
# Este metodo es para reemplazar, le vamos a dar un 
# texto que queremos que reemplaze y le vamos a decir
# que texto quiero poner ahi

print(myStr.replace('Hola', "Adios").upper())
print(" ")
# Metodos encadenados 
# Usamos replace para remplazar "Hola" y en su lugar 
# ponemos "Adios" luego usamos el metodo upper para 
# para cambiar todo a mayuscula

print(myStr.count("l"))
print(" ")
# Este metodo count cuenta las veces que usamos
# en este ejemplo la letra l 
# muestra 1 por que solo hay una L

print(myStr.startswith("hola"))
print(" ")
# Este metodo starswith es para saber si empieza con
# un determinado caracter
# en este caso da False
print(myStr.startswith("Hola"))
print(" ")
# Veamos si la variable myStr empieza con Hola
# En este caso da True

print(myStr.endswith("o"))
print(" ")
# El metodo endswith es para ver si la variable termina
# con el caracter
# En este caso da True

print(myStr.endswith("Soy"))
print(" ")
# En este caso no termina con el caracter soy 
# da False

print(myStr.split("e"))
print(" ")
# Separa y saca el caracter asignado 
# en este caso "e"

print(myStr.find('d'))
print(" ")
# Encuentra la posicion de la letra "d"

print(len(myStr))
print(" ")
# Impreme + Longitud de la cadena de texto

print(myStr.index("M"))
print(" ")
# Imprime indice de la letra M

print(myStr.isnumeric())
print(" ")
# Quiero saber si myStr es numerico

print(myStr.isalpha())
print(" ")
# Quiero saber si myStr es alfa numerico

print(myStr[15])
# Imprime + myStr + la posicion 15
print(myStr[-1])
# Imprime + myStr + la posicion -1
print(" ")
# Imprime + myStr + la posicion 

# Concatenacion 
print("Como te va " + myStr)
# con el signo de suma 
print(f"que onda 10 {myStr}")
# Con f y dentro de llaves {myStr}
print("¿Que haces carucha? {0}".format(myStr))
# imprimimos dentro de la cadena ponemos
# al final  la posicion de donde lo quiero 
# mostrar en la variable 
print(" ")

