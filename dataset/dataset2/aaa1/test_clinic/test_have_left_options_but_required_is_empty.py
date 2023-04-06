from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_have_left_options_but_required_is_empty():

    def fn():
        clinic.permute_optional_groups(['a'], [], [])
    ClinicGroupPermuterTest.assertRaises(AssertionError, fn)

ClinicGroupPermuterTest = test_clinic.ClinicGroupPermuterTest()
test_have_left_options_but_required_is_empty()
