from __future__ import print_function
import sys
if sys.executable.endswith("pythonw.exe"):
    sys.stdout = sys.stdout = None

print("can handle sys.stdout = None just fine.")