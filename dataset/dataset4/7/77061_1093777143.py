from idlelib.pyparse import Parser
import timeit
code='def f():\n'
print(timeit.timeit("statement",  # for example
                    "p=Parser(4,4)", globals = globals()))