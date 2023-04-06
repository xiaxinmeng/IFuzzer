@singledispatch
def fun(a):
    print('base case')

@fun.register(A)
def _(a):
    print('fun A')