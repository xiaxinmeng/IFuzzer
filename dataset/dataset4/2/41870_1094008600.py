def replace(self, old, new):
    result = []
    for elem in self:
        if elem == old:
            result.append(new)
        else:
            result.append(elem)
    self[:] = result