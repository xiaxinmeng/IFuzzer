
def take_first(it: Iterable):
    # if `it` is empty, StopIteration will be raised accidentally
    return next(it) 

iterables = [iter([1]), iter([]), iter([2, 3])] # the second one is empty
for i in map(take_first, iterables):
    print(i)
