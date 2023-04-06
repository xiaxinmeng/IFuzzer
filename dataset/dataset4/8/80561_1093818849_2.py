def __setitem__(self, elem, count):
    if count <= 0:
        self._nonpositive.add(elem)
    else:
        self._nonpositive.discard(elem)
    return super().__setitem__(elem, count)