
import traceback
import sys

try:
    env = {}
    with open('script') as f:
        exec(f.read(), env)
except:
    type_, value_, tb = sys.exc_info()
    print (traceback.print_tb(tb))
