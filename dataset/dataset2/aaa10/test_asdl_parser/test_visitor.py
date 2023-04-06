import importlib.machinery
import importlib.util
import os
from os.path import dirname
import sys
import sysconfig
import unittest
import test_asdl_parser

def test_visitor():

    class CustomVisitor(TestAsdlParser.asdl.VisitorBase):

        def __init__(TestAsdlParser):
            super().__init__()
            TestAsdlParser.names_with_seq = []

        def visitModule(TestAsdlParser, mod):
            for dfn in mod.dfns:
                TestAsdlParser.visit(dfn)

        def visitType(TestAsdlParser, type):
            TestAsdlParser.visit(type.value)

        def visitSum(TestAsdlParser, sum):
            for t in sum.types:
                TestAsdlParser.visit(t)

        def visitConstructor(TestAsdlParser, cons):
            for f in cons.fields:
                if f.seq:
                    TestAsdlParser.names_with_seq.append(cons.name)
    v = CustomVisitor()
    v.visit(TestAsdlParser.types['mod'])
    TestAsdlParser.assertEqual(v.names_with_seq, ['Module', 'Module', 'Interactive', 'FunctionType'])

TestAsdlParser = test_asdl_parser.TestAsdlParser()
test_visitor()
