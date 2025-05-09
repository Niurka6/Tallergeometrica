class FiguraGeometrica:
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto

    @property
    def ancho(self):
        return self._ancho

    @property
    def alto(self):
        return self._alto

    @property
    def area(self):
        return self._ancho * self._alto

    @property
    def perimetro(self):
        return 2 * (self._ancho + self._alto)

    def area (self):
        return self._ancho * self._alto

    def perimetro (self):
        return 2 * (self._ancho + self._alto )

    def __str__(self):
        return f"Figura Geometrica: {self.__dict__.__str__()}"

if __name__ == "__main__":
    fg = FiguraGeometrica(8, 2)
    print(fg)
    print(f"Área: {fg.area()}")
    print(f"Perímetro: {fg.perimetro()}")