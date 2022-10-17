# Ejercicio 01: Crear una funcion para sumar los valores
# recibidos de tipo numericos, utilizando argumentos variables *args como parametros de la 
# Funcion y agregar como resultado la suma de todos los valores pasados
# como argumentos


def suma_valor(*args): # Recibimos una cantidad de parametros indefinidos
    resultado = 0
    # Iteramoscada elemento
    for valor in args:
        resultado += valor
    return resultado
# Llamamos a la funcion
print(suma_valor(3, 5, 9, 2, 1))

