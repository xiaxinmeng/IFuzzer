import sys

atexit1 = sys.modules.pop('atexit', None)
if atexit1 is None:
    import atexit as atexit1
    del sys.modules['atexit']

import atexit as atexit2

atexit1.register(print, "atexit1 callback")
atexit2.register(print, "atexit2 callback")