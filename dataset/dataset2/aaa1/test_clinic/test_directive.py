from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest
import test_clinic

def test_directive():
    c = test_clinic.FakeClinic()
    parser = test_clinic.DSLParser(c)
    parser.flag = False
    parser.directives['setflag'] = lambda : setattr(parser, 'flag', True)
    block = clinic.Block('setflag')
    parser.parse(block)
    ClinicParserTest.assertTrue(parser.flag)

ClinicParserTest = test_clinic.ClinicParserTest()
test_directive()
