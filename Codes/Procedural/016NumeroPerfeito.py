#NumeroPerfeito

x = int(input("Insira um número: "))
y = 0
z = int(x/2 +1)

for i in range(1,z):
    if x%i == 0:
        y = y+i

if y == x:
    print("O número é perfeito.\n\n")
else:
    print("O número não é perfeito.\n\n")
