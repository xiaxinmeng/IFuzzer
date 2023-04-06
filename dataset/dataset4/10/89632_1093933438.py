for name, fun in namefun:
    name2fun[name] = lambda x, fun=fun: fun(x)