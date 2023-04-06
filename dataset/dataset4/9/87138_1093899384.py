import gc
import sys

gc.collect()
before = sys.gettotalrefcount()

import somemod
del sys.modules['somemod']
del somemod

gc.collect()
after = sys.gettotalrefcount()