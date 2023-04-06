def foo():
    try:
        print(new)
        for i in range(100):
            yield i
    except:
        yield from foo()

m = foo()
for i in m:
    print(i)
