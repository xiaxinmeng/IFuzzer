def g():
    yield 0

it = g()
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break