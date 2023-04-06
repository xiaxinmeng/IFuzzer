import os
import unittest
from test.support.import_helper import import_module
from test.support.os_helper import TESTFN, unlink

import test_msilib

def test_invalid_first_char():
    Test_make_id.assertEqual(msilib.make_id('9.short'), '_9.short')
    Test_make_id.assertEqual(msilib.make_id('.short'), '_.short')

Test_make_id = test_msilib.Test_make_id()
test_invalid_first_char()
