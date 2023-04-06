class blah:

    def __init__(self, items=[]):
        self.items = items

a = blah()
b = blah()

a.items.append("apples")
b.items.append("oranges")