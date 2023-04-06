import dis
import pickle
import unittest
from test.support import check_syntax_error
import test_positional_only_arg

def test_syntax_for_many_positional_only():
    fundef = 'def f(%s, /):\n  pass\n' % ', '.join(('i%d' % i for i in range(300)))
    compile(fundef, '<test>', 'single')

PositionalOnlyTestCase = test_positional_only_arg.PositionalOnlyTestCase()
test_syntax_for_many_positional_only()
