class Rectangulo: 
    """
    Crear uyna clase llamada Rectangulo, debe tener 2 atributos: altura y base
    el nombre del metodo sera calcular area utilizando la formula:
    area = base * altura. Pero la base y la altura deben ser ingresadas
    por el usuario y los objetos deben ser tres
    """
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def multiplicacion(self):
        return self.base * self.altura

calculo = int(input("Digite la base: "))
calculo1 = int(input("Digite la altura: "))
rectangulo = Rectangulo(calculo, calculo1)
print(f'El area del rectangulo es: {rectangulo.multiplicacion()}')
