class C:
    def __init__(self):
        self._value = 999

    @property
    def bar(self):
        return self._value

obj = C()
obj.bar  # returns 999