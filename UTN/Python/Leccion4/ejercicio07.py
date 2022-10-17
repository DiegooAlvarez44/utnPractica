# Ejercicio 7: Juego adivina el numero
# Realizar un juego para adivinar un numero. Para ello
# se debe generar un numero aleatorio 1 - 100, y luego ir pidiendo
# numeros indicando "es mayor" o "es menor" segun sea mayor o menor
# con respecto a N. El proceso termina cuando el usuario acierta
# y alli se debe mostrar el numero de intentos



import random

numeroAzar = random.randint(1, 100)
a = False
while a == False:
    numjugado = int(input("Adivine el numero: "))
    
    if numjugado > numeroAzar:
        print(f"El numero es Menor {numjugado} ")  
    elif numjugado < numeroAzar:
        print(f"El numero es Mayor que {numjugado}") 
    else:
        print("GANASTE!!!!")
        a = True

print(f"Felicidades el numero era {numeroAzar}")