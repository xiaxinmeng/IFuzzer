from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_multiline_substitution():
    ClinicLinearFormatTest._test('\n          abc\n          {name}\n          def\n          ', '\n          abc\n          bingle\n          bungle\n\n          def\n          ', name='bingle\nbungle\n')

ClinicLinearFormatTest = test_clinic.ClinicLinearFormatTest()
test_multiline_substitution()
