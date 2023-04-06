import faulthandler
import sys

sys.stderr = None

try:
	faulthandler.enable()
except:
	sys.stderr = sys.__stderr__
raise
