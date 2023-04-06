
def f(t=None):
    t0, t1 = t if t is not None else [], []
    return t0, t1


def g(t=None):
    if t is None:
        t = [], []
    t0, t1 = t
    return t0, t1


def test():
    res_f = f(t=([1, 1], [2, 2]))
    res_g = g(t=([1, 1], [2, 2]))
    assert res_f == res_g, f'{res_f=} != {res_g=}'


test()
