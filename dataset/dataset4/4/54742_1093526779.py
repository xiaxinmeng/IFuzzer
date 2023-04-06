from collections import defaultdict

class defaultdict_value(defaultdict):
    def __init__(self, value):
        defaultdict.__init__(self, lambda : value)

x = defaultdict_value(3)
print(x[1])