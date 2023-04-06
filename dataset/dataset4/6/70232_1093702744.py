__a = 3
print(locals())
class T:
    def __init__(self):
        global __a
        self.a = __a
t1 = T()