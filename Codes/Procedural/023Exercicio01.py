"""Desenvolva um banco de dados simples de forma que o usuário possa inserir um produto e seu preço,
além de poder consultar o preço de um produto, tudo isso sem quer que aceessar o arquivo
de texto"""


nomeArq = input("Insira o nome do arquivo: ")
x = input("Se quiser ler o arquivo, digite L. Se quiser escrever, digite E: ")

if x == "L":
    try:
        print("Abrindo arquivo...")
        arq = open(nomeArq, 'r')
        lista = arq.readlines()
        arq.close()
        print("Arquivo aberto.")
        x = input("Insira palavra chave do produto: ")
        for i in lista:
            if x in i:
                print(i)
    except:
        print("Arquivo não encontrado.")

    
elif x == "E" :
    x = int(input("Para adicionar uma linha no final digite 1, para substituir uma linha digite 2: "))
    if x == 1:
        try:
            print("abrindo arquivo...")
            arq = open(nomeArq, 'a')
            a = input("insira o nome do produto: ")
            b = input("insira o preço do produto: ")
            c = "%s R$:%s\n" %(a,b)
            arq.write(c)
            arq.close()
        except:
            print("Arquivo não encontrado, criando novo aquivo...")
            arq = open(nomeArq, 'w')
            a = input("insira o nome do produto: ")
            b = input("insira o preço do produto: ")
            c = "%s R$:%s\n" %(a,b)
            arq.write(c)
            arq.close()
            

    elif x==2:
        print("abrindo arquivo...")
        lista = open(nomeArq, 'r').readlines()
        open(nomeArq,'r').close()
        a = input("insira a palavra chave do produto: ")
        i = 0
        while a not in lista[i]:
            i = i+1
            if i > len(lista) :
                print("produto não encontrado.")
                break
        a = input("insira o nome do produto: ")
        b = input("insira o preço do produto: ")
        lista[i] = "%.12s R$:%s\n" %(a,b)
        arq = open(nomeArq, 'w')
        arq.write(lista)
        arq.close()
print("\n\nA seguir, o arquivo: \n")
arq = open(nomeArq, 'r')
lista=arq.readlines()
arq.close()
for i in range(len(lista)):
    print(lista[i])
        






        
        
