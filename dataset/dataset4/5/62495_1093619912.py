def f(*args, **kwargs): return len(args), len(kwargs)

f(*([0]*(2**32+1)))
f(**dict.fromkeys(map(hex, range(2**31+1))))