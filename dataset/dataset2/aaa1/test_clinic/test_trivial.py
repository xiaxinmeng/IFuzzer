from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_trivial():
    parser = DSLParser(FakeClinic())
    block = clinic.Block('module os\nos.access')
    parser.parse(block)
    (module, function) = block.signatures
    ClinicParserTest.assertEqual('access', function.name)
    ClinicParserTest.assertEqual('os', module.name)

ClinicParserTest = test_clinic.ClinicParserTest()
test_trivial()
