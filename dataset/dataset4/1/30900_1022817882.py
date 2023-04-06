
X = list["X"]
def f(x: X): ...
get_type_hints(f)  # hopefully no RecursionError
