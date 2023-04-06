import netrc, os, unittest, sys, tempfile, textwrap
from test import support
from test.support import os_helper
import test_netrc

def test_macros():
    nrc = NetrcTestCase.make_nrc('            macdef macro1\n            line1\n            line2\n\n            macdef macro2\n            line3\n            line4\n            ')
    NetrcTestCase.assertEqual(nrc.macros, {'macro1': ['line1\n', 'line2\n'], 'macro2': ['line3\n', 'line4\n']})

NetrcTestCase = test_netrc.NetrcTestCase()
test_macros()
