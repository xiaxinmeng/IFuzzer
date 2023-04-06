# prog.py
import sys

print(sys.version)
trace = sys.gettrace()
print("None traces:", trace.__self__.traces)
print("Hello")