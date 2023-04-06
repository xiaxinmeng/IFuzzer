import copy

def make_closure():
    closure = []
    def append(value):
        closure.append(value)
    return append, closure

func, closure = make_closure()
func(1)
func2 = copy.deepcopy(func)
func2(2)
print(func2 is func)
print(closure)