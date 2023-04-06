import re
import unittest
from test import support
from test import test_syntax
import test_syntax

def test_continue_outside_loop():
    SyntaxTestCase._check_error('if 0: continue', 'not properly in loop')
    SyntaxTestCase._check_error('if 0: continue\nelse:  x=1', 'not properly in loop')
    SyntaxTestCase._check_error('if 1: pass\nelse: continue', 'not properly in loop')
    SyntaxTestCase._check_error('class C:\n  if 0: continue', 'not properly in loop')
    SyntaxTestCase._check_error('class C:\n  if 1: pass\n  else: continue', 'not properly in loop')

SyntaxTestCase = test_syntax.SyntaxTestCase()
test_continue_outside_loop()
