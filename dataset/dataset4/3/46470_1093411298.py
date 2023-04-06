class A:
    a = 'test'
    def __g(a):
        for c in a:
            if c in a:
                yield c
    tuple(__g(a))