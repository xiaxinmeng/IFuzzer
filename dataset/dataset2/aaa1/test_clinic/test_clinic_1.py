from test import support, test_tools
from test.support import os_helper
from unittest import TestCase
import collections
import inspect
import os.path
import sys
import unittest
import test_clinic

def test_clinic_1():
    ClinicBlockParserTest._test_clinic('\n    verbatim text here\n    lah dee dah\n/*[copy input]\ndef\n[copy start generated code]*/\nabc\n/*[copy end generated code: output=03cfd743661f0797 input=7b18d017f89f61cf]*/\nxyz\n', '\n    verbatim text here\n    lah dee dah\n/*[copy input]\ndef\n[copy start generated code]*/\ndef\n/*[copy end generated code: output=7b18d017f89f61cf input=7b18d017f89f61cf]*/\nxyz\n')

ClinicBlockParserTest = test_clinic.ClinicBlockParserTest()
test_clinic_1()
