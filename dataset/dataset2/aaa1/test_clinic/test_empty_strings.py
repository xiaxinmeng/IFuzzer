from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_empty_strings():
    ClinicLinearFormatTest._test('', '')

ClinicLinearFormatTest = test_clinic.ClinicLinearFormatTest()
test_empty_strings()
