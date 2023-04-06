import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_max_lines_long():
    LongWordTestCase.check_wrap(LongWordTestCase.text, 12, ['Did you say ', '"supercalifr', 'agilisticexp', '[...]'], max_lines=4)

LongWordTestCase = test_textwrap.LongWordTestCase()
LongWordTestCase.setUp()
test_max_lines_long()
