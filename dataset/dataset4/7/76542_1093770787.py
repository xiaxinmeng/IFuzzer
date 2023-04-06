a = "a : global"
def f():
    a = "a : local to f"
    def g():
#        global a     # uncommenting this line causes a syntax error.
#        a = a+", modified in g"
        def h():
            nonlocal a
            a = a+", modified in h"
        h()
        print (f"in g : a = '{a}'")
    g()
    print (f"in f : a = '{a}'")
f()
print (f"glogal : a = '{a}'")