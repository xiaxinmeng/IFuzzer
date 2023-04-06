import operator

args = ("AAAA",)*0x10000000
ag = operator.methodcaller(*args)
