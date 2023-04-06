def foo(obj):
    for _ in range(10000):
        res = obj.index(42)
    return res