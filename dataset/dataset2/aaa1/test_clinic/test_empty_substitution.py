from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_empty_substitution():
    ClinicLinearFormatTest._test('\n          abc\n          {name}\n          def\n          ', '\n          abc\n          def\n          ', name='')

ClinicLinearFormatTest = test_clinic.ClinicLinearFormatTest()
test_empty_substitution()
