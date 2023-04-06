import gc
import pprint
import sys
import unittest
import pprint
import test_sys_setprofile

def test_caught_nested_exception():

    def f(p):
        try:
            1 / 0
        except:
            pass
    f_ident = test_sys_setprofile.ident(f)
    ProfileHookTestCase.check_events(f, [(1, 'call', f_ident), (1, 'return', f_ident)])

ProfileHookTestCase = test_sys_setprofile.ProfileHookTestCase()
test_caught_nested_exception()
