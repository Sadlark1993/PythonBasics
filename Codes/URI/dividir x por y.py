#dividir x po y

x = int(input())

for i in range(0,x):
    y = input()
    y = y.split()
    
    try:
        y = y + [float(y[0])/float(y[1])]
        print("%.1f" %y[2])
    except:
        print("divisao impossivel")
