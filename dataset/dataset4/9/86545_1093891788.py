class Obj:
    def __init__(self, num):
        self.num = num
        self.var = self.funct()
        
    def funct(self, array = []):
        array += [1,2,3] # issue also occurs with .append()
        return array
    
    
    
def main():
    obj1 = Obj(1)
    print (obj1.num, obj1.var) # prints: 1 [1, 2, 3]

    obj2 = Obj(2)
    
    print (obj1.num, obj1.var) # prints: 1 [1, 2, 3, 1, 2, 3]
    print (id(obj1), id(obj1.var)) # prints a unique address for obj1, but the address for the var attribute is the same as for obj2
    print (obj2.num, obj2.var) # prints: 2 [1, 2, 3, 1, 2, 3]
    print (id(obj2), id(obj2.var)) # prints a unique address for obj2, but the address for the var attribute is the same as for obj1
    
    
if __name__ == "__main__": 
    main()