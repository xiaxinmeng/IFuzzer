import sys
import os
modname = 'relpath'
filename = modname + '.py'
sys.path.insert(0, os.curdir)
with open(filename, "w") as fp:
    print("import sys", file=fp)
    print("mod = sys.modules[__name__]", file=fp)
    print("print(f'{__file__=}')", file=fp)
    print("print(f'{mod.__file__=}')", file=fp)
    print("print(f'{mod.__cached__=}')", file=fp)
__import__(modname)
os.unlink(filename)