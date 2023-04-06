from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_no_substitution():
    ClinicLinearFormatTest._test('\n          abc\n          ', '\n          abc\n          ')

ClinicLinearFormatTest = test_clinic.ClinicLinearFormatTest()
test_no_substitution()
