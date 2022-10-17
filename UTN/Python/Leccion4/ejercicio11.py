# Ejercicio 11: agenda telefonica
# Hacer un programa que simule una agenda de contactors.
# Crear un diccionario donde la clave sea el nombre del usuario
# y el valor sea el telefono, el programa tendra el siguiente menu de opciones:
#       1. Nuevo contacto
#       2. Borrar contacto
#       3. Ver contactos existentes
#       4. Salir


from ast import If
import telnetlib
from xml.etree import ElementInclude
agenda = {}
while True:
    print(".:Menu:.")
    print("1. Nuevo contacto")
    print("2. Borrar contacto")
    print("3. Ver contactos existentes")
    print("4. Salir")
    opcion = int(input("Seleccione lo que quiera hacer: "))
    if (opcion == 1): 
            nombre = (input("Escriba el nombre de su nuevo contacto: "))
            telefono = (input("Digite su numero: "))
            if nombre not in agenda:
                agenda[nombre] = telefono
                print("Contacto agregado exitosamente")
            else:
                print("El contacto ya existe")
    elif (opcion == 2):
                nombre = input("Cual es el nombre del contacto: ")
                if nombre in agenda:
                    del (agenda[nombre])
                    print('Se ha eliminado el contacto')
                else:
                    print('Este contacto no existe')
    elif (opcion == 3):
                for clave, valor in agenda.items():
                    print(f"Nombre: {nombre}, telefono: {valor}")
    elif (opcion == 4):
            print("Programa terminado")
False