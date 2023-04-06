from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_right_only():
    ClinicGroupPermuterTest._test([], [], [['a'], ['b'], ['c']], ((), ('a',), ('a', 'b'), ('a', 'b', 'c')))

ClinicGroupPermuterTest = test_clinic.ClinicGroupPermuterTest()
test_right_only()
