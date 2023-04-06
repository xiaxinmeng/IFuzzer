import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_function_type():
    for function_type in ('() -> int', '(int, int) -> int', '(Callable[complex], More[Complex(call.to_typevar())]) -> None'):
        UnparseTestCase.check_ast_roundtrip(function_type, mode='func_type')

UnparseTestCase = test_unparse.UnparseTestCase()
test_function_type()
