import sys
import traceback
try:
	raise ValueError()
except:
	exctype, value, tb = sys.exc_info()
	traceback.print_tb(tb)
