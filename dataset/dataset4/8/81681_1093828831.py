import dis
import sys

print(sys.version)

def with_if_0():
    print(1)
    if 0:
        print(2)
    print(3)

dis.dis(with_if_0)