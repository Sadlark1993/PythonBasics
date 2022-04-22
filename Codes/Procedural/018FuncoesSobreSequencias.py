#SequenciasSobreFuncoes

def quadrado(x):
    return x*x

lista = [3, 4, 5, 6, 7]

lista2 = list(map(quadrado, lista))
print(lista2)

lista2 = list(map(quadrado, [4, 5, 6, 7]))
print(lista2)
