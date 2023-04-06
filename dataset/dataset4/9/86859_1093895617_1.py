def one():
    return 1

def two():
    return one() + 1

def const_test():
    if two() != 2:
       lots_of_code_here