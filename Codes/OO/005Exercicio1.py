"""Crie uma matilha de 100 cachorros, de modo que todos tenham nomes 'Dogj', sendo
j = 1, 2, 3,..., 100, e gere simultaneamente idade aleatória diferente para cada um deles."""

import random


class Dog:
    def __init__(self, nome):
        self.nome = nome
        self.idade = int(random.random()*12)
        self.coisa = 1
    print(self.coisa)
    

matilha = [Dog('Dog1')]
for i in range(1,100):    
    matilha += [Dog('Dog%i' %(i+1))]


print(matilha[15].nome, matilha[15].idade)
        
