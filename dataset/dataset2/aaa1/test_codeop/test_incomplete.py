import sys
import unittest
import warnings
from test import support
from test.support import warnings_helper
from codeop import compile_command, PyCF_DONT_IMPLY_DEDENT
import io
import test_codeop

def test_incomplete():
    ai = CodeopTests.assertIncomplete
    ai('(a **')
    ai('(a,b,')
    ai('(a,b,(')
    ai('(a,b,(')
    ai('a = (')
    ai('a = {')
    ai('b + {')
    ai('if 9==3:\n   pass\nelse:')
    ai('if 9==3:\n   pass\nelse:\n')
    ai('if 9==3:\n   pass\nelse:\n   pass')
    ai('if 1:')
    ai('if 1:\n')
    ai('if 1:\n pass\n if 1:\n  pass\n else:')
    ai('if 1:\n pass\n if 1:\n  pass\n else:\n')
    ai('if 1:\n pass\n if 1:\n  pass\n else:\n  pass')
    ai('def x():')
    ai('def x():\n')
    ai('def x():\n\n')
    ai('def x():\n  pass')
    ai('def x():\n  pass\n ')
    ai('def x():\n  pass\n  ')
    ai('\n\ndef x():\n  pass')
    ai('a = 9+ \\')
    ai("a = 'a\\")
    ai("a = '''xy")
    ai('', 'eval')
    ai('\n', 'eval')
    ai('(', 'eval')
    ai('(\n\n\n', 'eval')
    ai('(9+', 'eval')
    ai('9+ \\', 'eval')
    ai('lambda z: \\', 'eval')
    ai('if True:\n if True:\n  if True:   \n')
    ai('@a(')
    ai('@a(b')
    ai('@a(b,')
    ai('@a(b,c')
    ai('@a(b,c,')
    ai('from a import (')
    ai('from a import (b')
    ai('from a import (b,')
    ai('from a import (b,c')
    ai('from a import (b,c,')
    ai('[')
    ai('[a')
    ai('[a,')
    ai('[a,b')
    ai('[a,b,')
    ai('{')
    ai('{a')
    ai('{a:')
    ai('{a:b')
    ai('{a:b,')
    ai('{a:b,c')
    ai('{a:b,c:')
    ai('{a:b,c:d')
    ai('{a:b,c:d,')
    ai('a(')
    ai('a(b')
    ai('a(b,')
    ai('a(b,c')
    ai('a(b,c,')
    ai('a[')
    ai('a[b')
    ai('a[b,')
    ai('a[b:')
    ai('a[b:c')
    ai('a[b:c:')
    ai('a[b:c:d')
    ai('def a(')
    ai('def a(b')
    ai('def a(b,')
    ai('def a(b,c')
    ai('def a(b,c,')
    ai('(')
    ai('(a')
    ai('(a,')
    ai('(a,b')
    ai('(a,b,')
    ai('if a:\n pass\nelif b:')
    ai('if a:\n pass\nelif b:\n pass\nelse:')
    ai('while a:')
    ai('while a:\n pass\nelse:')
    ai('for a in b:')
    ai('for a in b:\n pass\nelse:')
    ai('try:')
    ai('try:\n pass\nexcept:')
    ai('try:\n pass\nfinally:')
    ai('try:\n pass\nexcept:\n pass\nfinally:')
    ai('with a:')
    ai('with a as b:')
    ai('class a:')
    ai('class a(')
    ai('class a(b')
    ai('class a(b,')
    ai('class a():')
    ai('[x for')
    ai('[x for x in')
    ai('[x for x in (')
    ai('(x for')
    ai('(x for x in')
    ai('(x for x in (')

CodeopTests = test_codeop.CodeopTests()
test_incomplete()
