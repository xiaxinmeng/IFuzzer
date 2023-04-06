class A:
    __slots__ = [
        "_color",
    ]

    color = None

    @property
    def color(self):
        return self._color