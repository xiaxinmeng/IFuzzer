import dis
import sys
print(sys.version)

def f():
    if __debug__:
        print("debug")
    else:
        print("not debug")
    if not __debug__:
        print("NOT DEBUG")
    else:
        print("DEBUG")

dis.dis(f)