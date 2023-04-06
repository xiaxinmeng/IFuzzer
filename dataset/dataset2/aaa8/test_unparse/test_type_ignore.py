import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_type_ignore():
    for statement in ('a = 5 # type: ignore', 'a = 5 # type: ignore and more', 'def x(): # type: ignore\n\tpass', 'def x(y): # type: ignore and more\n\tpass', 'async def x(): # type: ignore\n\tpass', 'async def x(y): # type: ignore and more\n\tpass', 'for x in y: # type: ignore\n\tpass', 'async for x in y: # type: ignore\n\tpass', 'with x(): # type: ignore\n\tpass', 'async with x(): # type: ignore\n\tpass'):
        UnparseTestCase.check_ast_roundtrip(statement, type_comments=True)

UnparseTestCase = test_unparse.UnparseTestCase()
test_type_ignore()
