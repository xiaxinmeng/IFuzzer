import itertools as it
args=["a"]*(2**16)
it.product(*args, repeat=2**16)