s1 = "hel"
s1 = intern(s1 + "lo")

class S(str):
    def __hash__(self):
        return 0
    def __eq__(self, other):
        return False

s = S(s1)
s2 = intern(s)
del s1