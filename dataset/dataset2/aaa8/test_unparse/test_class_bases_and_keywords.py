import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_class_bases_and_keywords():
    CosmeticTestCase.check_src_roundtrip('class X:\n    pass')
    CosmeticTestCase.check_src_roundtrip('class X(A):\n    pass')
    CosmeticTestCase.check_src_roundtrip('class X(A, B, C, D):\n    pass')
    CosmeticTestCase.check_src_roundtrip('class X(x=y):\n    pass')
    CosmeticTestCase.check_src_roundtrip('class X(metaclass=z):\n    pass')
    CosmeticTestCase.check_src_roundtrip('class X(x=y, z=d):\n    pass')
    CosmeticTestCase.check_src_roundtrip('class X(A, x=y):\n    pass')
    CosmeticTestCase.check_src_roundtrip('class X(A, **kw):\n    pass')
    CosmeticTestCase.check_src_roundtrip('class X(*args):\n    pass')
    CosmeticTestCase.check_src_roundtrip('class X(*args, **kwargs):\n    pass')

CosmeticTestCase = test_unparse.CosmeticTestCase()
test_class_bases_and_keywords()
