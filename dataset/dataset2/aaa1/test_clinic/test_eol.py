from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest

import test_clinic

def test_eol():
    c = clinic.Clinic(clinic.CLanguage(None), filename='file')
    raw = '/*[clinic]\nfoo\n[clinic]*/'
    cooked = c.parse(raw).splitlines()
    end_line = cooked[2].rstrip()
    ClinicWholeFileTest.assertNotEqual(end_line, '[clinic]*/[clinic]*/')
    ClinicWholeFileTest.assertEqual(end_line, '[clinic]*/')

ClinicWholeFileTest = test_clinic.ClinicWholeFileTest()
test_eol()
