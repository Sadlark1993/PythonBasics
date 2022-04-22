#herança e alguns métodos especiais

class OpBasicas:
    def __init__(self, entrada):
        self.valor = entrada
    def __add__(self, other):
        return self.valor + other.valor
    def __mul_(self, other):
        return self.valor + other.valor

class OpAvancadas(OpBasicas):
    def __init__(self, entrada): #nao seria necessario, pois o __init__ eh identico ao da classe pai
        self.valor = entrada
    def __div__(self,other):
        return float(self.valor)/(other.valor)

class OpExtras(OpAvancadas):
    def quadrado(self):
        return self.valor*self.valor

x = OpAvancadas(4)
y = OpAvancadas(3)

print(x.__div__(y))
