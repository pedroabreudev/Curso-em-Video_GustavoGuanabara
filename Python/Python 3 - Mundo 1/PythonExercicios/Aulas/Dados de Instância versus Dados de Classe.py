class FormaGeometrica:
    def desenha(self):
        pass


class Circulo(FormaGeometrica):
    PI = 3.14159

    def __init__(self, r):
        self.raio = r

    def desenha(self):
        pass

    def imprime(self):
        print("Círculo de raio {}".format(self.raio))

    def area(self):
        return Circulo.PI * (self.raio ** 2)

FormaGeometrica(Circulo)


