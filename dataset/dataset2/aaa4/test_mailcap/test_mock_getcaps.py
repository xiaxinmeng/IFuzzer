import mailcap
import os
import copy
import test.support
from test.support import os_helper
import unittest
import sys
import test_mailcap

def test_mock_getcaps():
    with os_helper.EnvironmentVarGuard() as env:
        env['MAILCAPS'] = test_mailcap.MAILCAPFILE
        caps = mailcap.getcaps()
        GetcapsTest.assertDictEqual(caps, test_mailcap.MAILCAPDICT)

GetcapsTest = test_mailcap.GetcapsTest()
test_mock_getcaps()
