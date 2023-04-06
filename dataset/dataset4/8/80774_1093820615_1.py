def trace(frame, event, arg):
    return trace

if len(sys.argv) > 1:
    sys.settrace(trace)

from unittest.mock import MagicMock

class A:
    pass

m = MagicMock(spec=A)
print("isinstance: ", isinstance(m, A))