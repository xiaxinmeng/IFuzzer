import inspect
class A:
    pass
print(inspect.getsource(A))
print(__name__)