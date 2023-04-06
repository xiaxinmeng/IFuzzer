@property
def hours(self):
    return self._seconds // 3600

@property
def minutes(self):
    return self._seconds // 60