__a = 3
print(locals())
class T:
    def __init__(self):
        m = sys.modules[__name__]
        self.a = m.__a
t3 = T()