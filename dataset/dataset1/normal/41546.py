from pprint import pprint
import traceback
import sys

# Writing messages to a file since we don't have a console window
f = open("output.txt", "w")

# No problem
print("print() test")

try:
	# This throws an exception, probably shouldn't
	pprint("pprint() test")
except Exception as e:
	f.write("A exception happened!\n")
	f.write(traceback.format_exc())
else:
	f.write("No exception happened.\n")

# This is probably the problem
f.write("sys.stdout = " + repr(sys.stdout) + "\n")

f.close()
