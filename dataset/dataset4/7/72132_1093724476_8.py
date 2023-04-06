class X(int):
    def __hash__(self):
        return 13 
    def __eq__(self, other):
        if len(d) > 1:
            d.clear()
        return False

d = {}
d = {X(1): 1, X(2): 2}
x = {}.fromkeys(d)