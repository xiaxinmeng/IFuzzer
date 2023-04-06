import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_simple_expressions_parens():
    CosmeticTestCase.check_src_roundtrip('(a := b)')
    CosmeticTestCase.check_src_roundtrip('await x')
    CosmeticTestCase.check_src_roundtrip('x if x else y')
    CosmeticTestCase.check_src_roundtrip('lambda x: x')
    CosmeticTestCase.check_src_roundtrip('1 + 1')
    CosmeticTestCase.check_src_roundtrip('1 + 2 / 3')
    CosmeticTestCase.check_src_roundtrip('(1 + 2) / 3')
    CosmeticTestCase.check_src_roundtrip('(1 + 2) * 3 + 4 * (5 + 2)')
    CosmeticTestCase.check_src_roundtrip('(1 + 2) * 3 + 4 * (5 + 2) ** 2')
    CosmeticTestCase.check_src_roundtrip('~x')
    CosmeticTestCase.check_src_roundtrip('x and y')
    CosmeticTestCase.check_src_roundtrip('x and y and z')
    CosmeticTestCase.check_src_roundtrip('x and (y and x)')
    CosmeticTestCase.check_src_roundtrip('(x and y) and z')
    CosmeticTestCase.check_src_roundtrip('(x ** y) ** z ** q')
    CosmeticTestCase.check_src_roundtrip('x >> y')
    CosmeticTestCase.check_src_roundtrip('x << y')
    CosmeticTestCase.check_src_roundtrip('x >> y and x >> z')
    CosmeticTestCase.check_src_roundtrip('x + y - z * q ^ t ** k')
    CosmeticTestCase.check_src_roundtrip('P * V if P and V else n * R * T')
    CosmeticTestCase.check_src_roundtrip('lambda P, V, n: P * V == n * R * T')
    CosmeticTestCase.check_src_roundtrip('flag & (other | foo)')
    CosmeticTestCase.check_src_roundtrip('not x == y')
    CosmeticTestCase.check_src_roundtrip('x == (not y)')
    CosmeticTestCase.check_src_roundtrip('yield x')
    CosmeticTestCase.check_src_roundtrip('yield from x')
    CosmeticTestCase.check_src_roundtrip('call((yield x))')
    CosmeticTestCase.check_src_roundtrip('return x + (yield x)')

CosmeticTestCase = test_unparse.CosmeticTestCase()
test_simple_expressions_parens()
