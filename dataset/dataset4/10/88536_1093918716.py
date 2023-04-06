iterable = iter(iterable)
current_min = next(iterable)
for x in iterable:
    if x < current_min:
        current_min = x
return current_min