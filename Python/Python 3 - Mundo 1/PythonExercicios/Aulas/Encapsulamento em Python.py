class Funcionario:
    def __init__(self, nome, cargo, valor_hora_trabalhada):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        self.__horas_trabalhadas = 0
        self.__salario = 0

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, novo_salario):
        raise ValueError("Impossível alterar salario diretamente. Use a funcao calcula_salario")

    def registra_hora_trabalhada(self):
        self.horas_trabalhadas += 1

    def cacula_salario(self):
        self.salario = self.horas_trabalhadas * self.valor_hora_trabalhada

pedro = Funcionario('Pedro', 'Gerente de Vendas', 50)
pedro.registra_hora_trabalhada(input(150))
pedro.cacula_salario(input(1000))
print(pedro.salario)

