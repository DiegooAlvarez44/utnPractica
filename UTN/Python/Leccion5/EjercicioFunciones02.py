# Ejercicio 2: Funcion con *args multiplicar
# Crear una funcion para multiplicar los valores recibidos
# de tipo numerico, utilizando argumentos varibales *args
# como parametro de la funcion y regresar como resultado
# la multiplicacion de todos los valores pasados como argumento




def multiplicacion(*args):
    resultado = 1
    for valor in args:
        resultado *= valor
    return resultado
print(multiplicacion(4, 5, 6, 44))
