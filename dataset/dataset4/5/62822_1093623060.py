def reset_mock(self, visited=None):
    "Restore the mock object to its initial state."
    if visited is None:
        visited = []
    if id(self) in visited:
        return