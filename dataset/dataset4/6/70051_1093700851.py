def __reversed__(self):
    return (self[k] for k in reversed(range(len(self))))