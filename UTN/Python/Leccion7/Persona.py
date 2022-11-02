
class Persona(): # Esta clase hereda de la clase Object
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __str__(self): # Override = sobreescribir
        return f'Persona:[ Nombre: {self._nombre}, Edad: {self._edad}]'

class Empleado(Persona): # La clase empleado es hija de la clase persona
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    @property
    def sueldo(self):
        return self._sueldo
    
    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

    



empleado1 = Empleado('Diego', 24, 75000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)
# Tarea: encapssular los atributos y agregar los metodos gatters and setters
# Crear otro objeto, pasar los datos para nombre, edad y sueldo
# Mostrar estos datos, luego modificar y mostrar nuevamente

empleado2 = Empleado('Fernando', 35, 85000)
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)

empleado3 = Empleado('Roberto', 44, 90000)
print(empleado3.nombre)
print(empleado3.edad)
print(empleado3.sueldo)