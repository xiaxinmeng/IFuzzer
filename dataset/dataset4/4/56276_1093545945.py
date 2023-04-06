class C():
    def __ge__(self, other):
        return True
    def __add__(self, other):
        return 44
    __radd__ = __add__

class O():
    pass  # removed NotImplemented defs
    
c = C()
o = O()
print(c >= o, o <= c)
# True True
print(c + o, o + c)
# 44 44