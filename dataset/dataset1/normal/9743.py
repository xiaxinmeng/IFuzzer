def crash():
    def a(): pass
    
    i = 0
    while i<1000:
        a = a.__call__
        
        i += 1
        if i % 1000 == 0:
            a()

crash()
