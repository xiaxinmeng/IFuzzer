class C:
    def __init__(self, cond):
        if cond:
            self.a = 1
        self.b = 2

c1 = C(True)
c2 = C(False)