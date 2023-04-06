from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_solo_newline():
    ClinicLinearFormatTest._test('\n', '\n')

ClinicLinearFormatTest = test_clinic.ClinicLinearFormatTest()
test_solo_newline()
