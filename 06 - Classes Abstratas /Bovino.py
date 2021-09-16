from Animal import Animal

class Bovino(Animal):

    def __init__(self, nome, idade):
        self.nome = nome
        self.__idade = idade

    @property
    def idade(self):
        logado = True
        if logado :
            return self.__idade

    @idade.setter
    def idade(self, valor):
        if valor >= 0:
            self.__idade = valor
        else:
            print( "Valor não permitido!" )

    def cadastrar(self):
        print( "Bovino ", self.nome, " cadastrado")
        self.somar()

    def somar(self):
        x = 2 + 2






