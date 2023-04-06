class F:
    def a(self):
        __x = None
        y = [[(__x:=2) for _ in range(2)] for __x in range(2)]
        print(y, __x)
F().a()