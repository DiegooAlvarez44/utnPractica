class Persona:
    def __init__(self, nombre, apellido, edad): # Se lo llama metodo Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self): #sekf es igual a this
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')


persona1 = Persona('Diego', 'Alvarez', 24) # Necesitamos enviar argumentos
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)

persona2 = Persona('Osvaldo', 'Giordanini', 45) # <__main__.Persona object at 0x0000022D416D1F48>
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} Su edad es: {persona2.edad}')


persona1.mostrar_detalle() #la referencia en este caso pasa de manera automatica
persona2.mostrar_detalle()

# Persona.mostrar_detalle(persona1) # Debemos pasarle una referencia para el self o dara error