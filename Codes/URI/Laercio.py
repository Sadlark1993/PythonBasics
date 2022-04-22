#Aquecimento OBI 2018 Fase Estadual: Laércio

n = 1

n = int(input())

for i in range(n):
    m = 0
    lista = 0
    
    m = int(input())
    lista = input()
    lista = lista.split()
    lista2 = []
    for j in range(m):
        if int(lista[j])%2:
            lista2 = lista2 + [int(lista[j])]
            
    while len(lista2):
        x = lista2[0]
        y = lista2[0]
        for j in range(len(lista2)):
            if lista2[j] > x:
                x = lista2[j]
            if lista2[j] < y:
                y = lista2[j]
        print("%i " %x, end = "")
        lista2.remove(x)
        if x != y:
            print("%i " %y, end = "")
            lista2.remove(y)
    print("")
        
        
