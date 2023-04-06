class MyFinder:
    def __init__(self, path):
        if path != "__myfinder__":
            raise ImportError()

    def find_module(self, fullname, path=None):
        return None

sys.path_hooks.append(MyFinder)
sys.path.insert(0, '__myfinder__')

import time
print('OK')