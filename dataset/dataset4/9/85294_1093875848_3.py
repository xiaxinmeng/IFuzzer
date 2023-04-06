plaintext

@functools.singledispatch
def negate_func(arg):
    raise NotImplementedError("can't negate")

@negate_func.register
def negate_int_func(arg:int):
    return -arg

@negate_func.register
def negate_bool_func(arg:bool):
    return not arg


if __name__ == "__main__":


    print(negate_func(0))
    print(negate_func(False))
    print(negate_func(arg=0))

