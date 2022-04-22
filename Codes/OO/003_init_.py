
import random

class Formas3d:
    def __init__(self, nome, tamanho, cor, arestas = 4):
        self.nome = nome
        self.tamanho = tamanho
        self.cor = cor
        self.arestas = arestas
    def updatePosition(self):
        self.position = random.random()*10, random.random()*10
        print('%s está agora em %s.' %(self.nome, self.position))



obj = Formas3d('quadrado', 3, 'azul', 4)
obj.updatePosition()
print(obj.position)
