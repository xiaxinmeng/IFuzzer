class C:
    def __instancecheck__(self, inst):
        raise RuntimeError(f'{self=}  {inst=}')

    
class P:
    def __instancecheck__(self, inst):
        raise RuntimeError(f'{self=}  {inst=}')

    
class C(P):
    pass