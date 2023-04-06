def outer(a):   
    def inner():
      print(a)  
      a = 43    
    return inner
                
t = outer(42)   
                
print(t())      