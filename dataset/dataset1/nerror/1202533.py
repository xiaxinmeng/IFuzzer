
Rec = 0

class X(Exception):
    def __new__(cls, *args):
        global Rec
        if Rec:
            Rec = 0
            return 5
        Rec = 1
        raise X

def f():
    raise X


try:
    f()
except ValueError:
    pass

 	  	 
