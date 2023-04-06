from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_legacy_converters():
    block = ClinicParserTest.parse('module os\nos.access\n   path: "s"')
    (module, function) = block.signatures
    ClinicParserTest.assertIsInstance(function.parameters['path'].converter, clinic.str_converter)

ClinicParserTest = test_clinic.ClinicParserTest()
test_legacy_converters()
