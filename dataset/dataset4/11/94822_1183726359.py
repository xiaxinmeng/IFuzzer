class M(type):
    pass
    
class C(metaclass=M):
    a = False

@property
def a(self):
    return True

for i in range(9):
    if i == 8:
        M.a = a
    print(C.a)