class Target:
    def __del__(self):
        print("The object is dead!")

def f():
    g()

def g():
    h()

def h():
    theobj = Target()
    theobj.thevalue