# Ejercicio 4: Sumar numeros pares dentro de un
# rango hacer un programa para sumar numeros pares
# dentro de un rango, por ejemplo
#                               suma de numeros pares del 2 al 30
#                               suma = 240

lista = range(1, 31)
suma = 0
for i in lista:
    if (i % 2 == 0):
        suma = i + i
    else:
        print(f"El numero {i} es impar no se suma")

print(suma)

###

a = int(input("Digite de donde va a comenzar la suma: "))
b = int(input("Digite hasta donde quiere llegar a sumar: "))
suma = 0
for i in range(a, b+1):
    if i % 2 == 0: 
        suma += i
print(f"La suma de numeros pares dentro del rango es: {suma}")