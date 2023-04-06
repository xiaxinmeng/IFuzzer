

def m1(arg):
    print(arg)
    def d1(func):
        print('d1')
        return func
    return d1

def m2(arg):
    print(arg)
    def d2(func):
        print('d2')
        return func
    return d2

@m1('one')
@m2('two')
class A:
    print('A')
