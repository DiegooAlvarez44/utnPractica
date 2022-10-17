class Cubo:
    """
    Crear la clase Cubo con los atributos, ancho, alto y profundidad, con un mentodo
    calcular_volumen que tendra la formula: 
    volumen = ancho * altura * profundidad
    que el usuario ingrese los valores
    """

    def __init__(self, altura, ancho, profundidad):
        self.altura = altura
        self.ancho = ancho
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.altura * self.ancho * self.profundidad

altura = float(input("Digite la altura: "))
ancho = float(input("Digite el ancho: "))
profundidad = float(input("Digite la profundidad: "))
cubo = Cubo(ancho, altura, profundidad)
print(f'El area del cubo es de {cubo.calcular_volumen()}')