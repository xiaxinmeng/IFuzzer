import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_roundtrip_mixed():
    for text in IndentTestCase.ROUNDTRIP_CASES:
        IndentTestCase.assertEqual(dedent(indent(text, ' \t  \t ')), text)

IndentTestCase = test_textwrap.IndentTestCase()
test_roundtrip_mixed()
