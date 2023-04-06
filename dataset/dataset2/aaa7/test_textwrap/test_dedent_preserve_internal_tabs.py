import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_dedent_preserve_internal_tabs():
    text = '  hello\tthere\n  how are\tyou?'
    expect = 'hello\tthere\nhow are\tyou?'
    DedentTestCase.assertEqual(expect, dedent(text))
    DedentTestCase.assertEqual(expect, dedent(expect))

DedentTestCase = test_textwrap.DedentTestCase()
test_dedent_preserve_internal_tabs()
