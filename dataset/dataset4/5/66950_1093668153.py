def izip(*args):
    iters = [iter(obj) for obj in args]
    while True:
        yield tuple(next(it) for it in iters)
x = izip([1,2],[3,4])
print(next(x)) #(1,3)
print(next(x)) #(2,4)
print(next(x)) #()