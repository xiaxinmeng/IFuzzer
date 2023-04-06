# a simple generator
def gen1():
    yield 1

# this generator pauses inside a 'try' block.
def gen2():
    try:
        yield 1
    finally:
        pass

def f(gen):
    g = gen()
    next(g)
    try:
        try:
            raise ValueError
        except:
            del g
            raise KeyError
    except Exception as e:
        print((e, e.__context__))

f(gen1) # Context OK
f(gen2) # No context
