class X():
    def __del__(self): 
        dict_b.clear()
    def __eq__(self, other):
        dict_a.clear()
        return True
    def __hash__(self): 
        return 13
        
dict_a = {X(): 0}
dict_b = {X(): X()}
dict_a == dict_b