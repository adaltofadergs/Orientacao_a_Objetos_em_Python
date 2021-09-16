from abc import ABCMeta, abstractmethod
class Animal(metaclass=ABCMeta):

    @property
    def idade(self):
        pass

    @idade.setter
    @abstractmethod
    def idade(self, valor):
        pass

    
    @abstractmethod
    def cadastrar(self):
        pass

    def somar(self):
        return 2 + 2





b = Bovino()

b.__idade = 5



print( b.idade ) 


b.idade = 2 