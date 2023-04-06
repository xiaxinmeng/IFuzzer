__a = 3
print(locals())
class T:
    def __init__(self):
        self.a = __a
t2 = T()