def foo():
    try:
        yield
    except BaseException as e:
        yield from foo()

for m in foo():
    print(i)