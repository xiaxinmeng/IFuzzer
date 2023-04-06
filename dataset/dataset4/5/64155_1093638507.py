import types
import inspect

class A:
    def say(self): print("A.say")
a = A()

class B: pass    
b = B()
b.say = types.MethodType(a.say, b)