#Reduce
import functools 


def soma(a, b):
    return a+b

print(functools.reduce(soma, [1,2,3,4,5]))

      
#ListCompreencions

x = [i*2 for i in [2,3,4]]
print(x)
