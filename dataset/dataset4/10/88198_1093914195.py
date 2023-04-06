import ast
import builtins
import sys
import os

tree = ast.parse("pass")
x = [tree]
x.append(x)

# Put the cycle somewhere to survive until the *last* GC collection
def callback(*args):
    pass
callback.a = x
os.register_at_fork(after_in_child=callback)