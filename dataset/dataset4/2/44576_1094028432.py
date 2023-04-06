s1 = "hel"
s1 = intern(s1 + "lo")

class S(str):
    def __hash__(self):
        return hash(s1)
    def __eq__(self, other):
        return other == s1

s = S("world")
intern(s)
del s1