import re
import unittest
from test import support
from test import test_syntax
import test_syntax

def test_assign_del():
    SyntaxTestCase._check_error('del (,)', 'invalid syntax')
    SyntaxTestCase._check_error('del 1', 'delete literal')
    SyntaxTestCase._check_error('del (1, 2)', 'delete literal')
    SyntaxTestCase._check_error('del None', 'delete None')
    SyntaxTestCase._check_error('del *x', 'delete starred')
    SyntaxTestCase._check_error('del (*x)', 'use starred expression')
    SyntaxTestCase._check_error('del (*x,)', 'delete starred')
    SyntaxTestCase._check_error('del [*x,]', 'delete starred')
    SyntaxTestCase._check_error('del f()', 'delete function call')
    SyntaxTestCase._check_error('del f(a, b)', 'delete function call')
    SyntaxTestCase._check_error('del o.f()', 'delete function call')
    SyntaxTestCase._check_error('del a[0]()', 'delete function call')
    SyntaxTestCase._check_error('del x, f()', 'delete function call')
    SyntaxTestCase._check_error('del f(), x', 'delete function call')
    SyntaxTestCase._check_error('del [a, b, ((c), (d,), e.f())]', 'delete function call')
    SyntaxTestCase._check_error('del (a if True else b)', 'delete conditional')
    SyntaxTestCase._check_error('del +a', 'delete operator')
    SyntaxTestCase._check_error('del a, +b', 'delete operator')
    SyntaxTestCase._check_error('del a + b', 'delete operator')
    SyntaxTestCase._check_error('del (a + b, c)', 'delete operator')
    SyntaxTestCase._check_error('del (c[0], a + b)', 'delete operator')
    SyntaxTestCase._check_error('del a.b.c + 2', 'delete operator')
    SyntaxTestCase._check_error('del a.b.c[0] + 2', 'delete operator')
    SyntaxTestCase._check_error('del (a, b, (c, d.e.f + 2))', 'delete operator')
    SyntaxTestCase._check_error('del [a, b, (c, d.e.f[0] + 2)]', 'delete operator')
    SyntaxTestCase._check_error('del (a := 5)', 'delete named expression')
    SyntaxTestCase._check_error('del a += b', 'invalid syntax')

SyntaxTestCase = test_syntax.SyntaxTestCase()
test_assign_del()
