import cgi
import os
import sys
import tempfile
import unittest
from collections import namedtuple
from io import StringIO, BytesIO
from test import support
import test_cgi

def test_log():
    cgi.log('Testing')
    cgi.logfp = StringIO()
    cgi.initlog('%s', 'Testing initlog 1')
    cgi.log('%s', 'Testing log 2')
    CgiTests.assertEqual(cgi.logfp.getvalue(), 'Testing initlog 1\nTesting log 2\n')
    if os.path.exists(os.devnull):
        cgi.logfp = None
        cgi.logfile = os.devnull
        cgi.initlog('%s', 'Testing log 3')
        CgiTests.addCleanup(cgi.closelog)
        cgi.log('Testing log 4')

CgiTests = test_cgi.CgiTests()
test_log()
