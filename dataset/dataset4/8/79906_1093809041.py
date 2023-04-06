def f():
    print('-- Start --')
    yield 1
    print('-- Middle --')
    yield 2
    print('-- Finished --')
    yield 3

gen = f()
for x in gen:
    print('Another things ...')
    next(gen)