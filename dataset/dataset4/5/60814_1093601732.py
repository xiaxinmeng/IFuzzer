def emptygen():
    # Or other more meaningful generator
    raise StopIteration
    yield

def wrap(gen):
    next(gen)
    print("This should be printed or StopIteration raised.")
    while True:
        try:
            yield next(gen)
        except StopIteration as exc:
            return

items = wrap(emptygen())
for item in items:
    print(item)

print("End.")