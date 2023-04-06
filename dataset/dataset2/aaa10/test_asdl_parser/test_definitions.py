import importlib.machinery
import importlib.util
import os
from os.path import dirname
import sys
import sysconfig
import unittest
import test_asdl_parser

def test_definitions():
    defs = TestAsdlParser.mod.dfns
    TestAsdlParser.assertIsInstance(defs[0], TestAsdlParser.asdl.Type)
    TestAsdlParser.assertIsInstance(defs[0].value, TestAsdlParser.asdl.Sum)
    TestAsdlParser.assertIsInstance(TestAsdlParser.types['withitem'], TestAsdlParser.asdl.Product)
    TestAsdlParser.assertIsInstance(TestAsdlParser.types['alias'], TestAsdlParser.asdl.Product)

TestAsdlParser = test_asdl_parser.TestAsdlParser()
test_definitions()
