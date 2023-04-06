import gc
import pprint
import sys
import unittest
import pprint
import test_sys_setprofile

def test_raise_reraise():

    def f(p):
        try:
            1 / 0
        except:
            raise
    f_ident = test_sys_setprofile.ident(f)
    ProfileHookTestCase.check_events(f, [(1, 'call', f_ident), (1, 'return', f_ident)])

ProfileHookTestCase = test_sys_setprofile.ProfileHookTestCase()
test_raise_reraise()
