def empty_with_docstring():
    '''Docstring'''

def docstring():
    '''Docstring'''
    return 1

import dis, sys

print(sys.version)

for fn in [empty, empty_with_docstring, docstring]:
    print(fn.__name__)
    dis.dis(fn)