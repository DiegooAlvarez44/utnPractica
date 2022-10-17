# Ejercicio 6: Tabla de multiplicar
# Hacer un programa que pida un numero por teclado
# y guarde en una lista su tabla de multiplicar hasta el 10
# Por ejemplo 
# Si digita el 5 la lista tendra: 5,10,15,20,25,30,35,40,45,50

lista = range(1, 11)
num = int(input("Digite un numero para multiplicar: "))
for i in lista:
    resultado = num * i
    print(resultado, end=("-"))

print(resultado)
