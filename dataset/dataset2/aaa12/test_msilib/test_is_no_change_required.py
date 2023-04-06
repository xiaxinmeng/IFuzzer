import os
import unittest
from test.support.import_helper import import_module
from test.support.os_helper import TESTFN, unlink

import test_msilib

def test_is_no_change_required():
    Test_make_id.assertEqual(msilib.make_id('short'), 'short')
    Test_make_id.assertEqual(msilib.make_id('nochangerequired'), 'nochangerequired')
    Test_make_id.assertEqual(msilib.make_id('one.dot'), 'one.dot')
    Test_make_id.assertEqual(msilib.make_id('_'), '_')
    Test_make_id.assertEqual(msilib.make_id('a'), 'a')

Test_make_id = test_msilib.Test_make_id()
test_is_no_change_required()
