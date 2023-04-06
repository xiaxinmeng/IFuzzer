import sys
import unittest
import warnings
from test import support
from test.support import warnings_helper
from codeop import compile_command, PyCF_DONT_IMPLY_DEDENT
import io
import test_codeop

def test_invalid():
    ai = CodeopTests.assertInvalid
    ai('a b')
    ai('a @')
    ai('a b @')
    ai('a ** @')
    ai('a = ')
    ai('a = 9 +')
    ai('def x():\n\npass\n')
    ai('\n\n if 1: pass\n\npass')
    ai('a = 9+ \\\n')
    ai("a = 'a\\ ")
    ai("a = 'a\\\n")
    ai('a = 1', 'eval')
    ai('a = (', 'eval')
    ai(']', 'eval')
    ai('())', 'eval')
    ai('[}', 'eval')
    ai('9+', 'eval')
    ai('lambda z:', 'eval')
    ai('a b', 'eval')
    ai('return 2.3')
    ai('if (a == 1 and b = 2): pass')
    ai('del 1')
    ai('del (1,)')
    ai('del [1]')
    ai("del '1'")
    ai('[i for i in range(10)] = (1, 2, 3)')

CodeopTests = test_codeop.CodeopTests()
test_invalid()
