def my_map(func, items):
    acc = []
    for item in items:
        if func == None:
            acc.append(item)
        else:
            acc.append(func(item))
    return acc