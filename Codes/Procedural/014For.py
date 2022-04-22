a = ['maca', 'banana', 'figo', 'manga']

for i in a:
    print(i)

print("\n")
for i in range(0,5,1):
    print(i)

print("\n se o primeiro e o ultimo numero for 0 e 1, pode ocultar: ")

for i in range(5):
    print(i)

matriz = [[1,0,0],[0,1,0],[0,0,1]]

for i in range(len(matriz)):
    print("\n")
    for j in range(len(matriz)):
        print (matriz[i][j], end = "") #o "end" eh pra nao quebrar a linha automaticamente


