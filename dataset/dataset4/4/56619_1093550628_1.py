timeout(5, """if 1:
   import os, sys
   ...
   do_something()
   ...
   sys.exit(0)
""")