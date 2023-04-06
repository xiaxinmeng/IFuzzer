def repeat(object, *times):
    if not times:
        while True:
            yield object
    elif len(times) == 1:
        for i in range(times[0]):
            yield object
    else:
        raise TypeError(f'There can be at most 1 times argument, not {len(times)}')