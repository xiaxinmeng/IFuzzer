import dis
POP_TOP = dis.opmap['POP_TOP']
wordcode = bytes([POP_TOP, 0] * 10)
f = lambda: None
f.__code__ = f.__code__.replace(co_code=wordcode)
f()