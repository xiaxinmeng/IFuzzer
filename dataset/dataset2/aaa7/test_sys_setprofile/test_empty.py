import gc
import pprint
import sys
import unittest
import pprint
import test_sys_setprofile

def test_empty():
    TestGetProfile.assertIsNone(sys.getprofile())

TestGetProfile = test_sys_setprofile.TestGetProfile()
test_empty()
