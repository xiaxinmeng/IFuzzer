from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_ludicrous():
    ClinicGroupPermuterTest._test([['a1', 'a2', 'a3'], ['b1', 'b2']], ['c1'], [['d1', 'd2'], ['e1', 'e2', 'e3']], (('c1',), ('b1', 'b2', 'c1'), ('b1', 'b2', 'c1', 'd1', 'd2'), ('a1', 'a2', 'a3', 'b1', 'b2', 'c1'), ('a1', 'a2', 'a3', 'b1', 'b2', 'c1', 'd1', 'd2'), ('a1', 'a2', 'a3', 'b1', 'b2', 'c1', 'd1', 'd2', 'e1', 'e2', 'e3')))

ClinicGroupPermuterTest = test_clinic.ClinicGroupPermuterTest()
test_ludicrous()
