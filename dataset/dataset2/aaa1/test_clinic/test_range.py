from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_range():
    ClinicGroupPermuterTest._test([['start']], ['stop'], [['step']], (('stop',), ('start', 'stop'), ('start', 'stop', 'step')))

ClinicGroupPermuterTest = test_clinic.ClinicGroupPermuterTest()
test_range()
