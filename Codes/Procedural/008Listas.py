#lista eh como chamam os vetores aqui

lista = [1, 2, 3]
print(lista)
print(lista[0] + lista[2])

lista = lista+[5]
print(lista)

lista = lista+[0, 0, 0]
print(lista)

print(lista[2:4])

#O ultimo elemento é chamado de -1, o penultimo de -2
#lembre-se que o python endereca os intervalos entre as variaves da lista
print(lista[2:-1])

lista[0] = "zero"
print(lista)
print(len(lista))

#nao eh possivel reatribuir o valor de um elemento de uma string, de uma lista eh possivel
