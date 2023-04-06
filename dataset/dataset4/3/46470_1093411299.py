class A:
    a = 'test'
    def __g(_x):
        for c in _x:
            if c in a:
                yield c
    tuple(__g(a))