
class Sizeable(object):
    def __instancecheck__(cls, instance):
        print("__instancecheck__ call")
        return hasattr(instance, "__len__")

class B(object):
    pass

b = B()
print(isinstance(b, Sizeable)) # output:False
