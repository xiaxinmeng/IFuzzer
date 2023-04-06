class A:
    def __init__(self, name):
        print("init {!r}".format(self))
        self.name = name
    def __repr__(self):
        return "I am {}".format(self.name)