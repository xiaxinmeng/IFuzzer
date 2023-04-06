import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_indent_nomargin_all_lines():
    predicate = lambda line: True
    for text in IndentTestCase.CASES:
        IndentTestCase.assertEqual(indent(text, '', predicate), text)

IndentTestCase = test_textwrap.IndentTestCase()
test_indent_nomargin_all_lines()
