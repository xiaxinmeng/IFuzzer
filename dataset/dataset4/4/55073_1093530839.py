import time
t = (12345,) + (0,)*8
print(repr(time.strftime("%Y", t)))