import sys
try:
    raise Exception("hm!")
except:
    t, v, tb = sys.exc_info()
    raise v