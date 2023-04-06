
try:
    first = next(iterable)
except StopIteration:
    print("Empty")
else:
    for item in itertools.chain([first], iterable):
        print(item)
    else:
        print("Ended naturally - non-empty.")
