import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_unary_op_factor():
    for prefix in ('+', '-', '~'):
        CosmeticTestCase.check_src_roundtrip(f'{prefix}1')
    for prefix in ('not',):
        CosmeticTestCase.check_src_roundtrip(f'{prefix} 1')

CosmeticTestCase = test_unparse.CosmeticTestCase()
test_unary_op_factor()
