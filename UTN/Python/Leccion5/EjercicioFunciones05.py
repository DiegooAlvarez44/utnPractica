# Ejercicio 5: Convertidor de temperaturas
# Realizar dos funciones para convertir grados celsius
# a fahrenheit y viseversa.
# Investigar las formulas


def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32 


def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

fahrenheit = float(input('Digite el valor de fahrenheit: '))
resultado = fahrenheit_celsius(fahrenheit)
print(f'{fahrenheit} C a F -> {resultado:.2f}') 


celsius = float(input('Digite el valor de celsius: '))
resultado = celsius_fahrenheit(celsius)
print(f'{celsius} C a F -> {resultado:.2f}')