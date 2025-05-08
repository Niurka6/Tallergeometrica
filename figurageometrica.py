class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

# Ejemplo de uso
rectangulo = Rectangulo(9, 2)
print("Área del rectángulo:", rectangulo.area())
print("Perímetro del rectángulo:", rectangulo.perimetro())

cuadrado = Cuadrado(10)
print("Área del cuadrado:", cuadrado.area())
print("Perímetro del cuadrado:", cuadrado.perimetro())