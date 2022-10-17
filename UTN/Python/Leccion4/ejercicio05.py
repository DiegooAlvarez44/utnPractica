# Ejercicoo 5: Factorial de un numero positivo
# Hacer un programa parqa calcular efactorial de un numero positvo



num = int(input("Digite un numero: "))
while num < 0:
    print("El numero tiene que ser positivo picaron")
    num = int(input("Digite un numero"))
factorial = 1
for i in range(1, num+1):
    factorial *= i
print(f"El factorial del numero {num} positivo ingresado es : {factorial} ")