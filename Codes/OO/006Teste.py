
# Program to demonstrate 'Variable  
# defined inside the method' 
  
# print("Inside_method1", inside_method) # Error 
  
'''class one'''
class Geek: 
    print() 
# print("Inside_method2", inside_method) # Error 
  
    def access_method(self): 
  
        # Variable defined inside the method. 
        inVar = 'inside_method'
        print("Inside_method3", inVar) 
  
uac = Geek() 
uac.access_method() 
  
'''class two'''
class AnotherGeek: 
    print() 
# print("Inside_method4", Inside_method) # Error 
  
    def access_method(self): 
        print() 
# print("Inside_method5", Inside_method) # Error 
  
uaac = AnotherGeek() 
uaac.access_method() 
