def cancel(self):
    if self.done():
        return False
    at_least_one_child_cancelled = False
    for child in self._children:
        if child.cancel():
            at_least_one_child_cancelled = True
    return at_least_one_child_cancelled