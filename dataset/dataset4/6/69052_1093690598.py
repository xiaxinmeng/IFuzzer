import sys
import traceback

import pdb;pdb.Pdb(stdout=sys.stderr).set_trace()
try:
    print("What... is your quest?")
except:
    sys.stderr.write("Exception in program.\n")
    traceback.print_exc(file=sys.stderr)