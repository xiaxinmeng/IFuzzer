import unittest
import test_decorators

def test_expressions():
    for expr in ('(x,)', '(x, y)', 'x := y', '(x := y)', 'x @y', '(x @ y)', 'x[0]', 'w[x].y.z', 'w + x - (y + z)', 'x(y)()(z)', '[w, x, y][z]', 'x.y'):
        compile(f'@{expr}\ndef f(): pass', 'test', 'exec')

TestDecorators = test_decorators.TestDecorators()
test_expressions()
