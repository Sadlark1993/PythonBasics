#Funções

def quadrado(x):
    return x*x

print(quadrado(4))

def somatorio(*y):
    soma = 0
    for i in y:
        soma = soma + i
    return soma

print(somatorio(1, 2, 3, 4, 5))
