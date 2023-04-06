import gc
import pprint
import sys
import unittest
import pprint
import test_sys_setprofile

def test_unbound_method_no_keyword_args():
    kwargs = {}

    def f(p):
        dict.get(**kwargs)
    f_ident = test_sys_setprofile.ident(f)
    ProfileSimulatorTestCase.check_events(f, [(1, 'call', f_ident), (1, 'return', f_ident)])

ProfileSimulatorTestCase = test_sys_setprofile.ProfileSimulatorTestCase()
test_unbound_method_no_keyword_args()
