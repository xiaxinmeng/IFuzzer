while elems:
    elem = elems.pop()
    changed = optimize(elem)
    if changed:
        elems.update(neighbors(elem))