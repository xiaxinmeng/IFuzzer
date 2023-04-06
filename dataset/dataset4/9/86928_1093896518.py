def foo():
    try:
        yield
    except:
        yield from foo()

for m in foo():
    print(i)