class Retangulo:
    def __init__(self, altura = 0, largura = 0):
        self.altura = altura
        self.largura = largura
        self.imprimir()

    def calcularArea(self):
        return self.altura * self.largura

    def calcularPerimetro(self):
        return (self.altura + self.largura) * 2

    def imprimir(self):
        print("Altura: " , self.altura , "\nLargura: ", self.largura)
    


