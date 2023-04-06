import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_slices():
    UnparseTestCase.check_src_roundtrip('a[1]')
    UnparseTestCase.check_src_roundtrip('a[1, 2]')
    UnparseTestCase.check_src_roundtrip('a[(1, *a)]')

UnparseTestCase = test_unparse.UnparseTestCase()
test_slices()
