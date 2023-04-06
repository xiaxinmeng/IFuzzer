from thread import start_new
from traceback import print_exc
def f():
 try: typo
 except: print_exc()
start_new(f, ())