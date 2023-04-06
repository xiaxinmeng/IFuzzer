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

@run_with_locale('LC_NUMERIC', 'en_US.UTF8')
def test_float__format__locale():
    for i in range(-10, 10):
        x = 1234567890.0 * 10.0 ** i
        TypesTests.assertEqual(locale.format_string('%g', x, grouping=True), format(x, 'n'))
        TypesTests.assertEqual(locale.format_string('%.10g', x, grouping=True), format(x, '.10n'))

TypesTests = test_types.TypesTests()
test_float__format__locale()
