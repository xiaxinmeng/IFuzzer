class A:
    def f(*args):
            print(super().__repr__())

A().f()
