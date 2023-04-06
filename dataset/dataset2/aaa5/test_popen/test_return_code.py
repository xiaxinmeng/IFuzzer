import unittest
from test import support
import os, sys
import test_popen

def test_return_code():
    PopenTest.assertEqual(os.popen('exit 0').close(), None)
    status = os.popen('exit 42').close()
    if os.name == 'nt':
        PopenTest.assertEqual(status, 42)
    else:
        PopenTest.assertEqual(os.waitstatus_to_exitcode(status), 42)

PopenTest = test_popen.PopenTest()
test_return_code()
