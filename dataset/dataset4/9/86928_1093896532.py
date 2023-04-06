import gc

DEPTH = 100

def foo():
    global DEPTH
    try:
        yield
    except BaseException as e:
        DEPTH -= 1
        if DEPTH < 1:
            return
        gc.collect()
        yield from foo()


def x():
    for m in foo():
        print(i)