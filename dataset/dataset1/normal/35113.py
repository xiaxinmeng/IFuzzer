import inspect

class Egg:

    def func(self):
        pass

class NestedA:

    class Egg:
        pass


print(inspect.getsource(NestedA.Egg))
print(inspect.getsource(Egg))
