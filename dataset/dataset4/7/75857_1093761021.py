import imp
import sys
print(sys.modules[__name__])
try:
    imp.load_source(__name__, __file__ + "\0")
except:
    pass
print(sys.modules[__name__])