import unittest
from textwrap import TextWrapper, wrap, fill, dedent, indent, shorten
import test_textwrap

def test_indent_no_lines():
    predicate = lambda line: False
    for text in IndentTestCase.CASES:
        IndentTestCase.assertEqual(indent(text, '    ', predicate), text)

IndentTestCase = test_textwrap.IndentTestCase()
test_indent_no_lines()
