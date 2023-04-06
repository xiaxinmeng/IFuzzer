from test.support import run_with_locale
import collections.abc
from collections import namedtuple
import inspect
import pickle
import locale
import sys
import types
import unittest.mock
import weakref
import typing
import test_types

def test_comparisons():
    if 0 < 1 <= 1 == 1 >= 1 > 0 != 1:
        pass
    else:
        TypesTests.fail('int comparisons failed')
    if 0.0 < 1.0 <= 1.0 == 1.0 >= 1.0 > 0.0 != 1.0:
        pass
    else:
        TypesTests.fail('float comparisons failed')
    if '' < 'a' <= 'a' == 'a' < 'abc' < 'abd' < 'b':
        pass
    else:
        TypesTests.fail('string comparisons failed')
    if None is None:
        pass
    else:
        TypesTests.fail('identity test failed')

TypesTests = test_types.TypesTests()
test_comparisons()
