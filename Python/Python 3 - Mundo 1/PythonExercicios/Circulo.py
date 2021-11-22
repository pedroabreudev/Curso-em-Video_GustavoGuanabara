#Classe do Objeto
class Circle:
    #Construtor
    def __init__(self, r):
        self.raio = r

    #Métodos da Classe
    def desenha(self):
        pass

    # Métodos da Classe
    def imprime(self):
        print("Círculo de raio {} nome do Arquivo é {}".format(self.raio, __name__))

v = Circle(8)
v.imprime()

