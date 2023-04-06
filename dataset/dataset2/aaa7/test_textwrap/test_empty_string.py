import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_empty_string():
    WrapTestCase.check_shorten('', 6, '')

WrapTestCase = test_textwrap.WrapTestCase()
WrapTestCase.setUp()
test_empty_string()
