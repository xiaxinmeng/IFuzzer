from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_add_window():
    ClinicGroupPermuterTest._test([['x', 'y']], ['ch'], [['attr']], (('ch',), ('ch', 'attr'), ('x', 'y', 'ch'), ('x', 'y', 'ch', 'attr')))

ClinicGroupPermuterTest = test_clinic.ClinicGroupPermuterTest()
test_add_window()
