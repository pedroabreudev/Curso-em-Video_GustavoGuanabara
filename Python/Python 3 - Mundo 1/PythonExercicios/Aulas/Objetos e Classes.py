class Circulo:
    def __init__(self, r):
        self.raio = r

    def dsenha(self):
        pass

    def imprime(self):
        print("Círculo de raio {}".format(self.raio))

obj_circulo = Circulo(5)
obj_circulo.imprime()
