
import sys

SRC = b"""\
def foo():
    '''

def bar():
    pass

def baz():
    '''quux'''
"""

try:
    exec(SRC)
except SyntaxError as e:
    print(
        f'{sys.version}\n\n'
        f'{type(e).__name__}:\n'
        f'- line: {e.lineno}\n'
        f'- offset: {e.offset}\n'
        f'- text: {e.text!r}\n'
    )
