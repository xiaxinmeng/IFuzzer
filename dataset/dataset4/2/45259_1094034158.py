def fun():
    abc = 1
    def fun2():
        print(abc)
    print(inspect.getsource(fun2))