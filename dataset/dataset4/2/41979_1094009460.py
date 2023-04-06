d = {} 
 
class test: 
        def __hash__(self): 
                d[self] = None 
 
d[test()] = None