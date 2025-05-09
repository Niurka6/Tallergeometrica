from color import Color
from FiguraGeometrica import FiguraGeometrica

class cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado=0, color=None):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def __str__(self):
        return f"Cuadrado -> {self.__dict__.__str__()}"

if __name__ == "__main__":
    c1 = cuadrado(lado=6, color="Rojo")
    print(c1)
    print(f"Área: {c1.area()}")
    print (f"Perimetro: {c1.perimetro()}")