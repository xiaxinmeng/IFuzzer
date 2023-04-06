class Obj:
    def __init__(self, num):
        self.num = num
        self.var = self.funct()
        
    def funct(self, array = []):
        print (array)
        array = [1,2,3]
        return array
    
    
    
def main():
    obj1 = Obj(1)
    print (obj1.num, obj1.var) # prints: 1 [1, 2, 3]


    obj2 = Obj(2)
    
    print (obj1.num, obj1.var) # prints: 1 [1, 2, 3, 1, 2, 3]
    print (obj2.num, obj2.var) # prints: 2 [1, 2, 3, 1, 2, 3]
    
    
if __name__ == "__main__": 
    main()