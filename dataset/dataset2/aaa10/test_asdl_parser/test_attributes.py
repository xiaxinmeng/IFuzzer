import importlib.machinery
import importlib.util
import os
from os.path import dirname
import sys
import sysconfig
import unittest
import test_asdl_parser

def test_attributes():
    stmt = TestAsdlParser.types['stmt']
    TestAsdlParser.assertEqual(len(stmt.attributes), 4)
    TestAsdlParser.assertEqual(repr(stmt.attributes[0]), 'Field(int, lineno)')
    TestAsdlParser.assertEqual(repr(stmt.attributes[1]), 'Field(int, col_offset)')
    TestAsdlParser.assertEqual(repr(stmt.attributes[2]), 'Field(int, end_lineno, opt=True)')
    TestAsdlParser.assertEqual(repr(stmt.attributes[3]), 'Field(int, end_col_offset, opt=True)')

TestAsdlParser = test_asdl_parser.TestAsdlParser()
TestAsdlParser.setUp()
test_attributes()
