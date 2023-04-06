class VerboseDel:
    def __del__(self):
        print("Goodbye Cruel World")
obj = VerboseDel()

def func():
    pass

import os
os.register_at_fork(after_in_child=func)
del os
del func

print("exit")