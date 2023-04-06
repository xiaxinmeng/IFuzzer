# Hack needed for:
#  python3 /tmp/b.py,
#  python3 -m /tmp/b
#  runpy.run_path('/tmp/b.py')
from os.path import dirname
__path__ = [dirname(__file__)]
del dirname

# Hack needed for:
#  python3 -m /tmp/b
if __name__ == '__main__' and not __package__:
    __package__ = '__main__'

from . import a

def g():
    print(a.FOO)

g()