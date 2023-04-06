import importlib.machinery
import importlib.util
import os
from os.path import dirname
import sys
import sysconfig
import unittest
import test_asdl_parser

def test_module():
    TestAsdlParser.assertEqual(TestAsdlParser.mod.name, 'Python')
    TestAsdlParser.assertIn('stmt', TestAsdlParser.types)
    TestAsdlParser.assertIn('expr', TestAsdlParser.types)
    TestAsdlParser.assertIn('mod', TestAsdlParser.types)

TestAsdlParser = test_asdl_parser.TestAsdlParser()
TestAsdlParser.setUp()
test_module()
