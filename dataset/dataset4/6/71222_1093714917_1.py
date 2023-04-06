def myexit():
  import sys
  sys.exit(2)

import atexit
atexit.register(myexit)