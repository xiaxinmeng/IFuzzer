import importlib.machinery
import importlib.util
import os
from os.path import dirname
import sys
import sysconfig
import unittest
import test_asdl_parser

def test_constructor_fields():
    ehandler = TestAsdlParser.types['excepthandler']
    TestAsdlParser.assertEqual(len(ehandler.types), 1)
    TestAsdlParser.assertEqual(len(ehandler.attributes), 4)
    cons = ehandler.types[0]
    TestAsdlParser.assertIsInstance(cons, TestAsdlParser.asdl.Constructor)
    TestAsdlParser.assertEqual(len(cons.fields), 3)
    f0 = cons.fields[0]
    TestAsdlParser.assertEqual(f0.type, 'expr')
    TestAsdlParser.assertEqual(f0.name, 'type')
    TestAsdlParser.assertTrue(f0.opt)
    f1 = cons.fields[1]
    TestAsdlParser.assertEqual(f1.type, 'identifier')
    TestAsdlParser.assertEqual(f1.name, 'name')
    TestAsdlParser.assertTrue(f1.opt)
    f2 = cons.fields[2]
    TestAsdlParser.assertEqual(f2.type, 'stmt')
    TestAsdlParser.assertEqual(f2.name, 'body')
    TestAsdlParser.assertFalse(f2.opt)
    TestAsdlParser.assertTrue(f2.seq)

TestAsdlParser = test_asdl_parser.TestAsdlParser()
test_constructor_fields()
