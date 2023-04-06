import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_empty_string_with_initial_indent():
    WrapTestCase.check_wrap('', 6, [], initial_indent='++')
    WrapTestCase.check_wrap('', 6, [], initial_indent='++', drop_whitespace=False)

WrapTestCase = test_textwrap.WrapTestCase()
test_empty_string_with_initial_indent()
