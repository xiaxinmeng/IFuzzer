def rv(items):
    for item in items[:]:  # iterate over a copy
        if not (item.isspace() or item == ''):
            items.remove(item)
    return items