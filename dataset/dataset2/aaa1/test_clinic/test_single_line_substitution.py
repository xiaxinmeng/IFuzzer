from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_single_line_substitution():
    ClinicLinearFormatTest._test('\n          abc\n          {name}\n          def\n          ', '\n          abc\n          GARGLE\n          def\n          ', name='GARGLE')

ClinicLinearFormatTest = test_clinic.ClinicLinearFormatTest()
test_single_line_substitution()
