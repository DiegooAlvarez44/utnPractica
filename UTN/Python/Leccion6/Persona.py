from logging.config import dictConfig


class Persona:
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs): # Se lo llama metodo Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self._dni = dni
        self.args = args
        self.wkargs = kwargs


    def mostrar_detalle(self): #sekf es igual a this
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self._dni}, la direccion es:  {self.args}, los datos importantes son {self.wkargs}')


persona1 = Persona('Diego', 'Alvarez', 24) # Necesitamos enviar argumentos
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona2 = Persona('Osvaldo', 'Giordanini', 45) # <__main__.Persona object at 0x0000022D416D1F48>
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} Su edad es: {persona2.edad}')


persona1.mostrar_detalle() #la referencia en este caso pasa de manera automatica
persona2.mostrar_detalle()

# Persona.mostrar_detalle(persona1) # Debemos pasarle una referencia para el self o dara error

persona1.telefono = '45652185'
print(f"Este es el telefono de {persona1.nombre} {persona1.telefono}") # Hemos creado un atributo de un objeto

persona3 = Persona("Rolando", "Romero", 4105051 ,22, "Telefono", "215445135", "Calle Lopez", 754, "Manzana", 34, 'Casa', 16, altura=1.85, Peso=85, Cfavorito="Azul")
persona3.mostrar_detalle()
# print(persona3._dni) Esta mal no se usa asi