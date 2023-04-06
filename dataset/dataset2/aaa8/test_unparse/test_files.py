import unittest
import test.support
import pathlib
import random
import tokenize
import ast
import test_unparse

def test_files():
    for item in DirectoryTestCase.files_to_test():
        if test.support.verbose:
            print(f'Testing {item.absolute()}')
        with DirectoryTestCase.subTest(filename=item):
            source = test_unparse.read_pyfile(item)
            DirectoryTestCase.check_ast_roundtrip(source)

DirectoryTestCase = test_unparse.DirectoryTestCase()
test_files()
