from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_ignore_line():
    block = ClinicParserTest.parse('#\nmodule os\nos.access')
    (module, function) = block.signatures
    ClinicParserTest.assertEqual('access', function.name)
    ClinicParserTest.assertEqual('os', module.name)

ClinicParserTest = test_clinic.ClinicParserTest()
test_ignore_line()
