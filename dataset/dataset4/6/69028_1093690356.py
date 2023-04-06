from enum import Enum

class Bool(Enum):
    Yep = True
    Nope = False

for value in Bool:
    print('%18r is %r' % (value, bool(value)))