import re
import unittest
from test import support
from test import test_syntax
import test_syntax

def test_yield_outside_function():
    SyntaxTestCase._check_error('if 0: yield', 'outside function')
    SyntaxTestCase._check_error('if 0: yield\nelse:  x=1', 'outside function')
    SyntaxTestCase._check_error('if 1: pass\nelse: yield', 'outside function')
    SyntaxTestCase._check_error('while 0: yield', 'outside function')
    SyntaxTestCase._check_error('while 0: yield\nelse:  x=1', 'outside function')
    SyntaxTestCase._check_error('class C:\n  if 0: yield', 'outside function')
    SyntaxTestCase._check_error('class C:\n  if 1: pass\n  else: yield', 'outside function')
    SyntaxTestCase._check_error('class C:\n  while 0: yield', 'outside function')
    SyntaxTestCase._check_error('class C:\n  while 0: yield\n  else:  x = 1', 'outside function')

SyntaxTestCase = test_syntax.SyntaxTestCase()
test_yield_outside_function()
