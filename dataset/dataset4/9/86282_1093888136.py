import inspect
import tokenize
from pprint import pprint as pp

src=[
 'def f():\n',
 '    return 1\n',
 '    #that was fun',
 '\n',
 '#Now comes g\n',
 'def g():\n',
 '    return 2\n']