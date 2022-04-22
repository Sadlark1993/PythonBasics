#TratamentoDeErros
x = 0
for i in range(5):
    while 1:
        try:
            x = int(input("digite um numero para receber o seu inverso: "))
            break
        except:
            print("apenas inteiros!")

    print("o inverso eh", 1./x, "\n")
