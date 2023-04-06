import os, time
from importlib import import_module

files = os.listdir("C:/Programs/Python34/Lib")
excludes = {'antigravity.py', 'compileall.py', 'crypt.py', 'pty.py',
            'this.py', 'tty.py', '__phello__.foo.py'}
start = time.monotonic()
for name in files:
    if name.endswith('.py') and name not in excludes:
        try:
            import_module(name[:-3])
        except:
            print(name)
print(time.monotonic()-start)