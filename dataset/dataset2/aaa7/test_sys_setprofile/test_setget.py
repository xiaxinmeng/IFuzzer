import gc
import pprint
import sys
import unittest
import pprint
import test_sys_setprofile

def test_setget():

    def fn(*args):
        pass
    sys.setprofile(fn)
    TestGetProfile.assertIs(sys.getprofile(), fn)

TestGetProfile = test_sys_setprofile.TestGetProfile()
test_setget()
