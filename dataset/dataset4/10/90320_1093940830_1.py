class Desc:
    def __get__(self, obj, typ) -> int: pass

class Some:
    a = Desc()

s = Some()
reveal_type(s.a)     # N: Revealed type is "builtins.int"
reveal_type(Some.a)  # N: Revealed type is "builtins.int"