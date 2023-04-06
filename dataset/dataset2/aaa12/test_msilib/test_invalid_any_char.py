import os
import unittest
from test.support.import_helper import import_module
from test.support.os_helper import TESTFN, unlink

import test_msilib

def test_invalid_any_char():
    Test_make_id.assertEqual(msilib.make_id('.s\x82ort'), '_.s_ort')
    Test_make_id.assertEqual(msilib.make_id('.s\x82o?*+rt'), '_.s_o___rt')

Test_make_id = test_msilib.Test_make_id()
test_invalid_any_char()
