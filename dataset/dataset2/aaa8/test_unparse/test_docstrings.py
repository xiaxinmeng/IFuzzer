import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_docstrings():
    docstrings = ('"""simple doc string"""', '"""A more complex one\n            with some newlines"""', '"""Foo bar baz\n\n            empty newline"""', '"""With some \t"""', '"""Foo "bar" baz """', '"""\\r"""', '""""""', '"""\'\'\'"""', '"""\'\'\'\'\'\'"""', '"""🐍⛎𩸽üéş^\\\\X\\\\BB⟿"""', '"""end in single \'quote\'"""', '\'\'\'end in double "quote"\'\'\'', '"""almost end in double "quote"."""')
    for prefix in test_unparse.docstring_prefixes:
        for docstring in docstrings:
            UnparseTestCase.check_src_roundtrip(f'{prefix}{docstring}')

UnparseTestCase = test_unparse.UnparseTestCase()
test_docstrings()
