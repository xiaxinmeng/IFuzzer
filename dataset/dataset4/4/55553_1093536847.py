def splitpath(path):
    head, tail = split(path)
    if head == path:
        return [head]
    else:
        return splitpath(head) + [tail]