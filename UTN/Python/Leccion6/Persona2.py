from traceback import print_tb


class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
    

    def mostrar_detalles(self):
        print(f"Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}")

    @property #Decorador
    def nombre(slef): #Metodo Getter
        print('Usamos el metodo Get')
        return slef._nombre
        

    @nombre.setter
    def nombre(self, nombre): #Metodo Setter
        print('Usamos el metodo Set')
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad


    @edad.setter
    def edad(self, edad):
        self._edad = edad
    
    def __del__(self):
        print(f'Persona2: {self._nombre} {self._apellido} {self._edad} ')
    
if __name__ == '__main__':
    persona1 = Persona2('Diego', 'Alvarez', 24)    
    #print(persona1._nombre) #Esto no se debe hacer
    print(persona1.nombre) #Llamamos al metodo getter
    persona1.nombre = 'Pedro Pompin' # Llmamos el metodo setter
    print(persona1.nombre) # Otra vez al metodo getter
    print(persona1.mostrar_detalles()) # LLamamos el metodo para mostra detalles
    #Atributo read-only (Solo lectura)seria la edad por quie no tiene el metodo set
    print(persona1.edad)
    # Tarea crar tres objetos mas, utilizando los metodos getter and setter 
    # para modificar, y mostrar los cambios

    persona2 = Persona2('Meli', 'Arnola', 21)
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    persona2.nombre = 'Melisa'
    persona2.apellido = 'Arnolita'
    persona2.edad = 21
    print(persona2.mostrar_detalles())

    persona3 = Persona2('Carli', 'Fonseca', 23)
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    persona3.nombre = 'Carla'
    persona3.apellido = 'Fonseka'
    persona3.edad = 44

    print(persona3.mostrar_detalles())

    persona4 = Persona2('Leo', 'Cache', 30)
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    persona4.nombre = 'Leonel'
    persona4.apellido = 'Cachefo'
    persona4.edad = 25
    print(persona4.mostrar_detalles())

    print(__name__)







    
