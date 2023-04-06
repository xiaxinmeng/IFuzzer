def min2(x, y):
    return y if y < x else x

def max2(x, y):
    return x if y < x else y

def min_list(xs):
    return reduce(min2, xs)

def max_list(xs):
    return reduce(max2, xs)