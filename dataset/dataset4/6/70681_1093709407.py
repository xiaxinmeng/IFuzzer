class A(list):
    def __del__(self):
        next(it)

it = iter(A())
next(it)