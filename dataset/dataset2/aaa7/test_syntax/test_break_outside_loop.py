import re
import unittest
from test import support
from test import test_syntax
import test_syntax

def test_break_outside_loop():
    SyntaxTestCase._check_error('if 0: break', 'outside loop')
    SyntaxTestCase._check_error('if 0: break\nelse:  x=1', 'outside loop')
    SyntaxTestCase._check_error('if 1: pass\nelse: break', 'outside loop')
    SyntaxTestCase._check_error('class C:\n  if 0: break', 'outside loop')
    SyntaxTestCase._check_error('class C:\n  if 1: pass\n  else: break', 'outside loop')

SyntaxTestCase = test_syntax.SyntaxTestCase()
test_break_outside_loop()
