def _uniq(items):
    newitems = []
    seen = set()
    for item in items:
        if item not in seen:
            newitems.append(item)
            seen.add(item)
    return newitems