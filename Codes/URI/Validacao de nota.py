


x=0
y=0
i = 1
j =1

while j:
    while i:
        x = float(input())
        if x<0 or x>10:
            print("nota invalida")
        else:
            i = 0
    i = 1

    while i:
        y = float(input())
        if y<0 or y>10:
            print("nota invalida")
        else:
            i = 0
    print("media = %.2f" %((x+y)/2) )
    i = 1
    while i:
        print("novo calculo (1-sim 2-nao)")
        x = int (input())
        if x<3 and x>0:
            i =0
    if x == 2:
        j = 0
    i = 1

