import importlib.machinery
import importlib.util
import os
from os.path import dirname
import sys
import sysconfig
import unittest
import test_asdl_parser

def test_product():
    alias = TestAsdlParser.types['alias']
    TestAsdlParser.assertEqual(str(alias), 'Product([Field(identifier, name), Field(identifier, asname, opt=True)])')

TestAsdlParser = test_asdl_parser.TestAsdlParser()
test_product()
