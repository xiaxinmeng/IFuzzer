import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_type_comments():
    for statement in ('a = 5 # type:', 'a = 5 # type: int', 'a = 5 # type: int and more', 'def x(): # type: () -> None\n\tpass', 'def x(y): # type: (int) -> None and more\n\tpass', 'async def x(): # type: () -> None\n\tpass', 'async def x(y): # type: (int) -> None and more\n\tpass', 'for x in y: # type: int\n\tpass', 'async for x in y: # type: int\n\tpass', 'with x(): # type: int\n\tpass', 'async with x(): # type: int\n\tpass'):
        UnparseTestCase.check_ast_roundtrip(statement, type_comments=True)

UnparseTestCase = test_unparse.UnparseTestCase()
test_type_comments()
